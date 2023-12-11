#!/usr/bin/node
/* Write a script that computes and prints a factorial */
const factorial = function (x) {
  if (isNaN(x) || x <= 1) {
    return 1;
  }
  return (x * factorial(x - 1));
};
const allArgs = process.argv.slice(2);
console.log(factorial(parseInt(allArgs[0])));
