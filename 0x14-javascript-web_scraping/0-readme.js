#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const filename = process.argv[2];
console.log(fs.readFileSync(filename, 'utf8'));
