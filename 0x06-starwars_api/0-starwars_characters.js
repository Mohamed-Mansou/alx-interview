#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const films = `https://swapi-api.hbtn.io/api/films/${id}`;

request(films, (err, res, body) => {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
