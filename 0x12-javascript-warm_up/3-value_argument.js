#!/usr/bin/node
let count = -2;
process.argv.forEach((val, index) => {
  count++;
});

if (count === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
