#!/usr/bin/node
const argv = process.argv;
const line = [];
const x = parseInt(argv[2]);
if (Number.isInteger(x) === false) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    line.push('X');
  }
  for (let i = 0; i < x; i++) {
    console.log(line.join(''));
  }
}
