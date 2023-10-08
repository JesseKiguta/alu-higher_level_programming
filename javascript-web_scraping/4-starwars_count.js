#!/usr/bin/node
const request = require('request');
const firstarg = process.argv[2];
request(firstarg, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const data = JSON.parse(body);
  let count = 0;
  for (const movie of data.results) {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
});
