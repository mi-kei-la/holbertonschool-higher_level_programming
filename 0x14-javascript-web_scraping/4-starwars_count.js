#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
var count = 0;

request.get(url, function (response, body) {
  const films = (JSON.parse(body.body).results);
  for (const film in films) {
    for (const char in films[film].characters) {
      if (films[film].characters[char].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
