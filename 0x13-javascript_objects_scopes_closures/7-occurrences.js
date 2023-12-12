#!/usr/bin/node
/* Function that searches occurence of element in a list */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
