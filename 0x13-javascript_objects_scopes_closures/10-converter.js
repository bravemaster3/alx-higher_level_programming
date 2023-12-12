#!/usr/bin/node
/* base conversion using closure */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
