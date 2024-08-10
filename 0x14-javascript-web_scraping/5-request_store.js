#!/usr/bin/node

const fs = require('fs');
const axios = require('axios');
const argv = process.argv;

axios
  .get(argv[2])
  .then(res => {
    fs.writeFile(argv[3], res.data, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(error => {
    console.log(`code: ${error.response.status}`);
  });
