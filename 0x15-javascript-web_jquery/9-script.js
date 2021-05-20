$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (trans) {
      $('DIV#hello').append(trans.hello);
    }
  });
});
