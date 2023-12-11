#!/usr/bin/node
/* Write a script that searches the second biggest integer in the list of arguments */
const allArgs = process.argv.slice(2);
let sec = 0;
let first;
let swap;
if (allArgs.length > 1) {
  first = allArgs[0]; /* Number.MIN_SAFE_INTEGER */
  sec = allArgs[1];
  if (sec > first) {
    swap = first;
    first = sec;
    sec = swap;
  }
  for (const i in allArgs) {
    if (parseInt(allArgs[i]) > first) {
      sec = first;
      first = parseInt(allArgs[i]);
    }
    if (parseInt(allArgs[i]) !== first && parseInt(allArgs[i]) > sec) {
      sec = parseInt(allArgs[i]);
    }
  }
}
console.log(sec);
