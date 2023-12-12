#!/usr/bin/node
/* function that returns the reversed version of a list */

exports.esrever = function (list) {
  const listr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listr.push(list[i]);
  }
  return listr;
};
