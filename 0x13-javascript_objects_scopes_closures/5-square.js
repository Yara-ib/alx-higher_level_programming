#!/usr/bin/node

// class Square that defines a square
// & inherits from Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (w) {
    super(w, w);
    this.size = w;
  }
}

module.exports = Square;
