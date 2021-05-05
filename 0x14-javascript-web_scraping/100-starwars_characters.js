#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, function (response, body) {
  const movie = JSON.parse(body.body);
  for (const char in movie.characters) {
    request.get(movie.characters[char], function (response, body) {
      const movieChar = JSON.parse(body.body);
      console.log(movieChar.name);
    });
  }
});
