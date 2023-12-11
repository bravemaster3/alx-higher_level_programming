#!/usr/bin/node
/* Write a script that prints two arguments passed to it, in the following format: “ is ” */
const allArgs = process.argv.slice(2);
console.log(`${allArgs[0]} is ${allArgs[1]}`);
