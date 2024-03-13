#!/usr/bin/node

// Script that imports an array and computes a new array.
const list = require('./100-data.js').list;
console.log(list);

const arr = list.map((value, index) => value * index);
console.log(arr);
