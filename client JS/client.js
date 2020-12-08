const http = require("http")

var msg = ""

function sendResquest(msg) {
    let body = JSON.stringify({
      sender: "toto",
      message: msg
    })
    let options = {
      hostname: "localhost",
      port: "5005",
      path: "/webhooks/rest/webhook",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(body)
      }
    }
    http
      .request(options, res => {
        let data = ""
        res.on("data", d => {
          data += d
        })
        res.on("end", () => {
          console.log(data)
        })
      })
      .on("error", console.error)
      .end(body)
}

var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line){
    console.log()
    sendResquest(line)
})
