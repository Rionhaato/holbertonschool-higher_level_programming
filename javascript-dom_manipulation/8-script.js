document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then((translation) => {
      const helloContainer = document.querySelector('#hello');

      helloContainer.textContent = translation.hello;
    });
});
