#!/usr/bin/node
/* Write a script that prints the addition of 2 integers */
const add = function (a, b) {
  return a + b;
};
const allArgs = process.argv.slice(2);
console.log(add(parseInt(allArgs[0]), parseInt(allArgs[1])));
