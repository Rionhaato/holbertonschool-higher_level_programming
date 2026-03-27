const updateB = document.querySelector('#update_header');
const headerNode = document.querySelector('header');

updateB.addEventListener('click', () => {
  headerNode.textContent = 'New Header!!!';
});