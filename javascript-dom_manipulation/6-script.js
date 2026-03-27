fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(CharacterData => {
    const characterBox = document.querySelector('#character');
    characterBox.textContent = CharacterData.name;
  });
