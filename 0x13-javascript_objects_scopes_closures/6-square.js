#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// class Square that defines a square
// & inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    } else {
      c = 'C';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
