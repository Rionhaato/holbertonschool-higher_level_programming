fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then((movieData) => {
    const moviesList = document.querySelector('#list_movies');

    movieData.results.forEach((film) => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      moviesList.appendChild(listItem);
    });
  });
