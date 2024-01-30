#!/usr/bin/node
const process = require('process');
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, response, body) => {
  if (!error) {
    const responseBody = JSON.parse(body);
    console.log(responseBody.title);
  }
});
