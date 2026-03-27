const redHeaderControl = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderControl.addEventListener('click', () => {
  headerElement.classList.add('red');
});
