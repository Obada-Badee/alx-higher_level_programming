#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length === 2) {
  console.log('Not a number');
} else {
  const ans = Math.floor(args[2]);
  if (isNaN(ans)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${ans}`);
  }
}
