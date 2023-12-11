#!/usr/bin/node
/* Write a script that prints a square */
const x = process.argv[2];
if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('X'.repeat(x));
  }
}
