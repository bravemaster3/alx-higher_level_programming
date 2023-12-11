#!/usr/bin/node
/* Write a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer: */
const allArgs = process.argv.slice(2);
const isInt = function (myVal) {
  /* return (/^\d+.*$/.test(myVal)); */
  return !isNaN(parseInt(myVal));
};
let msg;
if (isInt(allArgs[0])) {
  msg = `My number: ${parseInt(allArgs[0])}`;
} else {
  msg = 'Not a number';
}
console.log(msg);
