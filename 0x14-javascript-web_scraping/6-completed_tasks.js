#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const masterDict = {};

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let count = 0;
  const ret = JSON.parse(body);
  let lastId = ret[0].userId;
  for (const task in ret) {
    if (ret[task].userId !== lastId) {
      if (count !== 0) {
        masterDict[lastId] = count;
      }
      lastId++;
      count = 0;
    }
    if (ret[task].completed === true) {
      count++;
    }
  }
  masterDict[lastId] = count;
  console.log(masterDict);
});
