#!/usr/bin/node
/* class Square that inherits from Rectangle */
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
