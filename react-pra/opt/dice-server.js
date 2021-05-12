//httpモジュールを読み込む
const http =require('http')
const ctypr = {'Content-Type':'text/html;charset=utf-8'}

//Webサーバー実行
const svr = http.createServer(handler) //サーバー生成
svr.listen(8080) //ポート8080番で待ち受け開始

//サーバーにアクセスがあった時の処理
function handler (req,res){
    //URLの判断
    const url = req.url
    //トップページか？
    if (url ==='/' || url === '/index.html'){
        showIndexPage(req,res)
        return
    }
    //さいころページか？
    if (url.substr(0,6) === '/dice/'){
        showDicePage(req,res)
        return
    }
    //その他
    res.writeHead(404,ctypr)
    res.end('404 not found!')
}

//インデックスページにアクセスがあった時
function showIndexPage(req,res) {
    //httpヘッダーを出力
    res.writeHead(200,ctypr)
    const html = '<h1>さいころページの案内</h1>\n' +
                '<p><a href="/dice/6">6面体さいころ</a></p>' +
                '<p><a href="/dice/12">12面体さいころ</a></p>'
    res.end(html)
}

function showDicePage(req,res) {
    res.writeHead(200,ctypr)
    const a = req.url.split('/')
    const num = parseInt(a[2])
    const rnd = Math.floor(Math.random()*num)+1
    res.end('<p style="font-size:72px;">' + rnd + '</p>')
}
