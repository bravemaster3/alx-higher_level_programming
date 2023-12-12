#!/usr/bin/node
/* Write a script that imports an array and computes a new array. */
const list = require('./100-data.js').list;
console.log(list);
let i = 0;
const newList = list.map((x) => x * i++);
console.log(newList);
