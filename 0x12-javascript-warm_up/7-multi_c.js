#!/usr/bin/node
/* Write a script that prints x times “C is fun” */
const x = process.argv[2];
if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parseInt(x)) {
    console.log('C is fun');
    i++;
  }
}
