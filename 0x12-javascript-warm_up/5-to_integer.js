#!/usr/bin/node

const { argv } = require('node:process');

argv.length >= 3 && !isNaN(argv[2])
  ? console.log('My number: ' + argv[2].split('.')[0])
  : console.log('Not a number');
