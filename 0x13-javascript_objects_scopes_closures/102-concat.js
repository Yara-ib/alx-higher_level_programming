#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');

fs.readFile(argv[2], 'utf8', (err, data) => {
  error(err);
  fs.writeFile('./fileC', data, (err) => {
    error(err);
  });
});

fs.readFile(argv[3], 'utf8', (err, data) => {
  error(err);
  fs.writeFile('./fileC', data, { flag: 'r+' }, (err) => {
    error(err);
  });
});

function error (err) {
  if (err) {
    console.log(err);
  }
}
