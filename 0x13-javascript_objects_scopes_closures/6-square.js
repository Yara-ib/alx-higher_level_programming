#!/usr/bin/node

const Rectangle = require('./5-square');

// class Square that defines a square
// & inherits from Rectangle
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
