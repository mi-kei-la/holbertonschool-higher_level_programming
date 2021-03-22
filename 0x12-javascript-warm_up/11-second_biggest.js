#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    if (!isNaN(process.argv[i]));
    arr.push(parseInt(process.argv[i]));
  }
  arr = arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
