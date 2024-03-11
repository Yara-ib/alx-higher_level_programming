#!/usr/bin/node

const { argv } = require('node:process');

function check () {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('C is fun');
  }
}

!isNaN(argv[2]) ? check() : console.log('Missing number of occurrences');
