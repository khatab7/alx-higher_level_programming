#!/usr/bin/node

function factorial (number) {
  if (number <= 0 || Number.isInteger(number) === false) {
    return (1);
  }
  return (number * factorial(number - 1));
}

const argv = process.argv;

console.log(factorial(parseInt(argv[2])));
