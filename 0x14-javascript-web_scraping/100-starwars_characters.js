#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;

async function getData (url) {
  try {
    const res = await axios.get(url);
    return res.data;
  } catch (err) {
    console.error(err);
  }
}

const url = `https://swapi-api.hbtn.io/api/films/${argv[2]}`;
getData(url)
  .then(res => {
    res.characters.forEach((charac) => {
      getData(charac)
        .then(res => console.log(res.name));
    });
  });
