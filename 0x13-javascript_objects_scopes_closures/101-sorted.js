#!/usr/bin/node
/* script that imports a dictionary of occurrences by user id and computes
a dictionary of user ids by occurrence. */
const dict = require('./101-data.js').dict;
const newDict = {};
let val;
for (const key in dict) {
  val = dict[key];
  if (newDict[val] === undefined) {
    newDict[val] = [key];
  } else {
    newDict[val].push(key);
  }
}
console.log(newDict);
