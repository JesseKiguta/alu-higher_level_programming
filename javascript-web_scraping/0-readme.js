#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
