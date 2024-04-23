#!/usr/bin/node

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    for (const character in body.characters) {
      request(body.characters[character], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
