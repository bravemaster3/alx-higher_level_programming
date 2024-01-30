#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];
fs.writeFileSync(filename, content, 'utf-8');
