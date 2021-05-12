from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

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


f = drive.CreateFile({'title': 'TEST.TXT'})
f.SetContentString('Hello')
f.Upload()

print(f)