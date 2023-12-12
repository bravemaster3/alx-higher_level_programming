#!/usr/bin/node
/* Prints arguments */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
