#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    // for (let i = 0; i < results.length; i++){
    //     console.log(results[i].userId);
    // }
    const completedUsers = todos.reduce((acc, todo) => {
      if (todo.completed) {
        if (acc[todo.userId]) {
          acc[todo.userId]++;
        } else {
          acc[todo.userId] = 1;
        }
      }
      return acc;
    }, {});
    console.log(completedUsers);
  }
});
