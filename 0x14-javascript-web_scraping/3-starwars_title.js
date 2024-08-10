#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;

axios
  .get(`https://swapi-api.hbtn.io/api/films/${argv[2]}`)
  .then(res => {
    console.log(res.data.title);
  })
  .catch(error => {
    console.log(`code: ${error}`);
  });
