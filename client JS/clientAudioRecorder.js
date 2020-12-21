// Import module.
const fs = require('fs');
const readline = require("readline");
const AudioRecorder = require('node-audiorecorder');
const rq = require('http');

// Options is an optional parameter for the constructor call.
// If an option is not given the default value, as seen below, will be used.
const options = {
  program: 'arecord',     // Which program to use, either `arecord`, `rec`, or `sox`.
  device: 'hw:1,0',       // Recording device to use, e.g. `hw:1,0`

  bits: 16,           // Sample size. (only for `rec` and `sox`)
  channels: 1,        // Channel count.
  encoding: 'signed-integer',  // Encoding type. (only for `rec` and `sox`)
  format: 'S16_LE',   // Encoding type. (only for `arecord`)
  rate: 16000,        // Sample rate.
  type: 'wav',        // Format type.

  // Following options only available when using `rec` or `sox`.
  silence: 0,         // Duration of silence in seconds before it stops recording.
  thresholdStart: 0.5,  // Silence threshold to start recording.
  thresholdStop: 0.5,   // Silence threshold to stop recording.
  keepSilence: true   // Keep the silence in the recording.
};
// Optional parameter intended for debugging.
// The object has to implement a log and warn function.
const logger = console;

// Create an instance.


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const fileStream = fs.createWriteStream("input.wav", { encoding: 'binary' });

let audioRecorder = new AudioRecorder(options, logger);
function main(){
    rl.question("Record s/e ? ", function(input) {
            if(input == "s") {
    // Creates and starts the recording process.
                console.log("start")
                audioRecorder.start().stream().pipe(fileStream);
            }
            if(input == "e"){
    // Stops and removes the recording process.
                console.log("end")
                audioRecorder.stop();

                let buff = fs.readFileSync('input.wav')
                let data64 = buff.toString('base64')
                let params = Buffer.from("('shit': 111, 'rate': 16000)")
                let buffParam = params.toString('base64')

                const data = JSON.stringify({
                    wav: data64,
                    param: buffParam,
                })

                const opt = {
                    hostname: 'localhost',
                    port: 3211,
                    path: '/api',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Content-Length': data.length
                    }
                }
                let co = rq.request(opt, (res) => {
                    res.on('data', (d) => {
                        let response = JSON.parse(d.toString())
                        let transcription = response.text

                        call_rasa(transcription)
                    })
                })
                co.write(data)
                co.end()
            }
            main()
    });
}

function call_rasa(transcription) {
const dataRasa = JSON.stringify({
                            sender: "toto",
                            message: transcription,
                        })

                        const opt = {
                            hostname: 'localhost',
                            port: 5005,
                            path: '/webhooks/rest/webhook',
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'Content-Length': dataRasa.length
                            }
                        }
                        let rasa = rq.request(opt, (res) => {
                            res.on('data', (d) => {
                                resp = JSON.parse(d.toString())
                                console.log(resp)
                            })
                        })
                        rasa.write(dataRasa)
                        rasa.end()

}

main()

// Returns the stream of the recording process.
//audioRecorder.stream();