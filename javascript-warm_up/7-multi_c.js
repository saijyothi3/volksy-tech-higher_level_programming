#!/usr/bin/node
const a = Number.parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
