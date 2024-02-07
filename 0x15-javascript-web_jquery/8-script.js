#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  for (const film of films) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  }
});
