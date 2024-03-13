#!/usr/bin/node

const { argv } = require('node:process');

// Comparison Function been added because sort() only sort by strings
// So 4 will be > 11 which is incorrect
argv.length > 3
  ? console.log(
    argv
      .sort(function (a, b) {
        return a - b;
      })
      .reverse()[1]
  )
  : console.log(0);
