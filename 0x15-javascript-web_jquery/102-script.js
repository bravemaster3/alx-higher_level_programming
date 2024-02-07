#!/usr/bin/node
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lan}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
