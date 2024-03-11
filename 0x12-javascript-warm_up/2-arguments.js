#!/usr/bin/node
const { argv } = require('node:process');
argv.length > 3
  ? console.log('Arguments found')
  : argv.length > 2
    ? console.log('Argument found')
    : console.log('No argument');
