#!/usr/bin/node
if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
