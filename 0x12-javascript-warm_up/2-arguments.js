#!/usr/bin/node
/* Write a script that prints a message depending of the number of arguments passed: */
const allArgs = process.argv.slice(2);
let msg;
if (allArgs.length === 0) {
  msg = 'No argument';
} else if (allArgs.length === 1) {
  msg = 'Argument found';
} else {
  msg = 'Arguments found';
}
console.log(msg);
