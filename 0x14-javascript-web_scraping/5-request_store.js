#!/usr/bin/node

const url = process.argv[2];
const fileName = process.argv[3];

const fs = require('fs');
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
