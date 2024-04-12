#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log('0');
} else {
  let max;
  const arrayInt = [];
  for (let i = 2; i < argv.length; i++) {
    arrayInt[i - 2] = parseInt(argv[i]);
  }
  max = Math.max(...arrayInt);
  arrayInt.splice(arrayInt.indexOf(max), 1);
  max = Math.max(...arrayInt);
  console.log(max);
}
