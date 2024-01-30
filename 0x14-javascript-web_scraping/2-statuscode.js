#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];
request = new Request(url);
request(url, (error, response, body) => {
    console.log("code: ${response.statusCode}");
})
