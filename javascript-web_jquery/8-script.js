let movieTitle;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (movieTitle of data.results) {
    title = data.results[i].title;
    $('UL#list_movies').append(`<li>${title}</li>`);
  }
});
