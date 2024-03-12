#!/usr/bin/node

// Function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const idx in list) {
    if (list[idx] === searchElement) {
      count += 1;
    }
  }
  return count;
};
