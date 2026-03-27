const addItemButton = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addItemButton.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
