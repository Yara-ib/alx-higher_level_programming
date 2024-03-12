#!/usr/bin/node

const { argv } = require('node:process');

function forLoop () {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('X'.repeat(Number(argv[2])));
  }
}

!isNaN(argv[2])
  ? forLoop()
  : console.log('Missing size');
