#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    let charCount = 0;
    for (const film of films) {
      if (film.characters.some(character => character.endsWith('/18/'))) {
        charCount++;
      }
    }
    console.log(charCount);
  }
});
