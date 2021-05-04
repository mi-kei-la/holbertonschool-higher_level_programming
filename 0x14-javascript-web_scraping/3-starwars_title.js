#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const ret = JSON.parse(body);
  console.log(ret.title);
});
