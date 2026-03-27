const toggleButton = document.querySelector('#toggle_header');
const headerTag = document.querySelector('header');

toggleButton.addEventListener('click', () => {
  if (headerTag.classList.contains('green')) {
    headerTag.classList.remove('green');
    headerTag.classList.add('red');
  } else {
    headerTag.classList.remove('red');
    headerTag.classList.add('green');
  }
});
