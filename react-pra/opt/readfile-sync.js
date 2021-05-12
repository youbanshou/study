const fs = require('fs')

const data = fs.readFileSync('kakugen.txt','utf-8')
console.log(data)

fs.readFile('kakugen.txt','utf-8',readHandler)
function readHandler(err,data) {
    console.log(data)
}