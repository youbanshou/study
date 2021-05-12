import gspread
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pprint

import httplib2
import csv
import datetime
import calendar
import pandas as pd

def toAlpha2(num):
    i = int((num-1)/26)
    j = int(num-(i*26))
    Alpha = ''
    for z in i,j:
        if z != 0:
            Alpha += chr(z+64)
    return Alpha

# #年月社員リスト取得
# with open('社員リスト.csv',encoding="utf-8_sig") as f:
#     member_list = f.read()
# #カンマ区切りを配列に変換
# member_list = member_list.split(',')

print('半角で西暦を入力してください(例:2020)')
year = input('>> ')

print('半角で月を入力してください(例:12)')
month = input('>> ')

print(year + '年' + month +'月' +'でよろしいですか？')
input('よろしければEnterを押してください')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
json_keyfile_path = 'perfor-manage-koyo-28d598bd8327.json'

# サービスアカウントキーを読み込む
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_keyfile_path, scope)

# pydrive用にOAuth認証を行う
gauth = GoogleAuth()
gauth.credentials = credentials
drive = GoogleDrive(gauth)
gc = gspread.authorize(credentials)

folder_id = '12cKbBxqRzMt8Myu-gnWSLhl4DDY-Eo3e'
#新規作成
# f = drive.CreateFile({
#     'title': 'sample_spread',
#     'mimeType': 'application/vnd.google-apps.spreadsheet',
#     "parents": [{"id": folder_id}]})
# f.Upload()


# 作成したスプレッドシートの情報を出力
# pprint.pprint(f)

# ---- create Google Drive Service
http = httplib2.Http()
http = credentials.authorize(http)
service = build('drive', 'v2', http=http)

# ---- Copy the file on Google Drive
new_file_name = year[2:] + '年'+month +'月_実績管理'
new_file_body = {
    'title': new_file_name,
    "parents": [{"id": folder_id}]
}

# ファイルのコピー
base_workbook = gc.open_by_key('1YlepsCsh9mwZPMP53qGZiALqJbhHuUKukg1IfXmJflo')
new_file = service.files().copy(
    fileId="1YlepsCsh9mwZPMP53qGZiALqJbhHuUKukg1IfXmJflo", body=new_file_body, supportsTeamDrives=True
    ).execute()

wb = gc.open_by_key(new_file["id"])
#個人シート日数調整
month_max =calendar.monthrange(int(year), int(month))[1]
parson_ws = wb.get_worksheet(1)
if month_max != 31:

    body = {
        "requests": [
            {
                "deleteDimension": {
                    "range": {
                        "sheetId": parson_ws.id,
                        "dimension": "COLUMNS",
                        "startIndex": 3+month_max,
                        "endIndex": 34
                    }
                }
            }
        ]
    }
    res = wb.batch_update(body)


#メンバーの数だけコピー
member_list = ["荒川","松岡","右近","千葉","天羽","山本","松村"]
for item in member_list: 
    wb_list = wb.worksheets()
    wb.duplicate_sheet(source_sheet_id = parson_ws.id, new_sheet_name = item,insert_sheet_index = len(wb_list)-1)

samary_ws =  wb.get_worksheet(0)
all_data = samary_ws.range("A1:AL65")
#年月設定
all_data[1].value =year
all_data[39].value =month
first_day = calendar.monthrange(int(year), int(month))[0]
for i in range(len(member_list)):
    for j in range(3,65):
        for k in range(5):
            row = (j+1)
            
            if k ==0:
                last_day = 4 + 6- first_day                
                all_data[ j * 38 + k+3+i*5].value = "=SUM("+member_list[i]+"!"+toAlpha2(4)+ str(row) +":"+member_list[i]+"!"+toAlpha2(last_day)+ str(row)+")"
            else:
                
                all_data[ j * 38 + k+3+i*5].value = "=SUM("+member_list[i]+"!"+toAlpha2(last_day +1 )+ str(row) +":"+member_list[i]+"!"+toAlpha2(last_day+7)+ str(row)+")"
                last_day += 7


samary_ws.update_cells(all_data,value_input_option='USER_ENTERED')
print('成功')