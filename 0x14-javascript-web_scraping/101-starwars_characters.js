#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;

async function getCharacters () {
  try {
    const characList = await axios.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}`);
    for (const url of characList.data.characters) {
      const charac = await axios.get(url);
      console.log(charac.data.name);
    }
  } catch (err) {
    console.error(err);
  }
}

getCharacters();
