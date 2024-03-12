#!/usr/bin/node

const { argv } = require('node:process');

function factorial (x) {
  if (x <= 1 || isNaN(x)) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}

console.log(factorial(argv[2]));
