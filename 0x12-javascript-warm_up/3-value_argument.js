#!/usr/bin/node
/* Write a script that prints the first argument passed to it */
const allArgs = process.argv.slice(2);
let msg;
if (allArgs[0] === undefined) {
  msg = 'No argument';
} else {
  msg = allArgs[0];
}
console.log(msg);
