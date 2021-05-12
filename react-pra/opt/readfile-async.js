const fs = require('fs')

function readFileEX(fname) {
    return new Promise((resolve,reject)=>{
        fs.readFile(fname,'utf-8',(err,data)=>{
            resolve(data)
        })
    })
}

async function readAll() {
    const a = await readFileEX('a.txt')
    console.log(a)
    const b = await readFileEX('b.txt')
    console.log(b)
    const c = await readFileEX('c.txt')
    console.log(c)
}

readAll()