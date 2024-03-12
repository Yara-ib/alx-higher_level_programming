#!/usr/bin/node

const { argv } = require('node:process');
argv.length > 3 ? console.log(argv.sort().reverse()[1]) : console.log(0);
