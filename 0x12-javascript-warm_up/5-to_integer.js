#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);
if (Number.isInteger(num) === false) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
