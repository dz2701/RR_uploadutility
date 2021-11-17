const {Storage} = require('@google-cloud/storage');
const express = require("express")
const app = new express();
const readline = require("readline");
const {spawn} = require('child_process');
const port = 3000;

const storage = new Storage({
  keyFilename: "./reserverecord-b2de5-firebase-adminsdk-it3bz-1d2e467dab.json"
});

let bucketName = "gs://reserverecord-b2de5.appspot.com"


async function  uploadFile(file){

    // Uploads a local file to the bucket
    await storage.bucket(bucketName).upload(file, {
        // Support for HTTP requests made with `Accept-Encoding: gzip`
        gzip: true,
        // By setting the option `destination`, you can change the name of the
        // object you are uploading to a bucket.
        metadata: {
            // Enable long-lived HTTP caching headers
            // Use only if the contents of the file will never change
            // (If the contents will change, use cacheControl: 'no-cache')
            cacheControl: 'public, max-age=31536000',
        },
});

console.log(`${file} uploaded to ${bucketName}.`);
}


/*
prompt.start();

while(1){
  prompt.get(['artid'],function (err, res) {
    if(err) return 0;

    uploadFile(".."+res.artid+".json");
  })
}
*/

var server = app.listen(port, () => {console.log('\n****Reserve Record article upload Utility*****\nArticle ID: (exit for end)\n')});

var rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout
});

function waitForUserInput() {
  console.log("Article ID: \n");
  rl.question("", function(answer) {
    if (answer == "exit"){
        rl.close();
        server.close();
    } else {
        console.log(answer)
        try{
          uploadFile("../"+answer+".json").then(waitForUserInput());
        }catch(e){
          console.log(e);
          server.close();
        }
    }
  });
}

waitForUserInput()
