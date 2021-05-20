$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + language,
      success: function (salut) {
        console.log(salut.hello);
        $('DIV#hello').append(salut.hello);
      }
    });
  });
});
