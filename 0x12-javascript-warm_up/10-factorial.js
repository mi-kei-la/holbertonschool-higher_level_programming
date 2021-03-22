#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const num = parseInt(process.argv[2]);
  console.log(fact(num));
}

function fact (x) {
  if (x === 0) {
    return (1);
  } else if (x < 0) {
    return x / fact(x + 1);
  } else {
    return x * fact(x - 1);
  }
}
