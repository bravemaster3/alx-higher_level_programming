#!/usr/bin/node
$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
