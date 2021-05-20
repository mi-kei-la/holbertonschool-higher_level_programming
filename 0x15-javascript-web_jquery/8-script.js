$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (films) {
    $.each(films.results, function (idx, films) {
      $('UL#list_movies').append('<li>' + films.title + '</li>');
    });
  }
});
