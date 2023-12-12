#!/usr/bin/node
/* script that concatenates 2 files */
const fs = require('fs');
const args = process.argv.slice(2);
console.log(args[0]);
const fileA = fs.readFileSync(args[0]);
const fileB = fs.readFileSync(args[1]);
fs.writeFileSync(args[2], fileA + fileB);
