const fs = require('fs')

fs.readFile('kakugen.txt','utf-8',function(err,data){
    console.log(data)
})