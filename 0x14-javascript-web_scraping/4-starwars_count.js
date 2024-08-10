#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    let nb = 0;
    response.data.results.forEach(movie => {
      if (movie.characters.some(charac => charac.includes('18'))) { nb++; }
    });
    console.log(nb);
  });
