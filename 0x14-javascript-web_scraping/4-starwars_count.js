#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
