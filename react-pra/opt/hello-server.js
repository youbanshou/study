const http = require('http')
const svr = http.createServer(handler)
svr.listen(8080)

function handler (req,res){
    console.log('url:',req.url)
    console.log('method:',req.method)
    //httpヘッダー出力
    res.writeHead(200,{'Content-Type':'Text/html'})
    res.end('<h1>Hello, World!</h1>\n')

}