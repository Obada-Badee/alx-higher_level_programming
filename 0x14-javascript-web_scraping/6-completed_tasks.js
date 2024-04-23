#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const task in tasks) {
      if (dict[tasks[task].userId] === undefined) {
        dict[tasks[task].userId] = 1;
      } else {
        dict[tasks[task].userId]++;
      }
    }
    console.log(dict);
  }
});
