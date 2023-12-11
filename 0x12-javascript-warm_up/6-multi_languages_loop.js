#!/usr/bin/node
/*
Write a script that prints 3 lines using an array and loop:
The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
*/
const myStrings = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const i in myStrings) {
  console.log(myStrings[i]);
}
