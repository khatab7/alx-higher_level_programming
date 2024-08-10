#!/usr/bin/node

const axios = require('axios');
const argv = process.argv;
const users = {};

axios
  .get(argv[2])
  .then(res => {
    res.data.forEach(function (task) {
      if (task.completed === true) {
        if (users[task.userId] === undefined) {
          users[task.userId] = 0;
        }
        users[task.userId] += 1;
      }
    });
    console.log(users);
  });
