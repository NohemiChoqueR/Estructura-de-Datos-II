console.log("Script cargado");

const input = document.getElementById('search');
const ul = document.getElementById('results');

input.addEventListener('input', async () => {
  const q = input.value.trim();
  if (!q) {
    ul.hidden = true;
    return;
  }

  try {
    const urlSugerencias = input.dataset.url;
const res = await fetch(`${urlSugerencias}?q=${q}&limit=5`);

    const list = await res.json();
    console.log(list);

    if (!list.length) {
      ul.hidden = true;
      return;
    }

    ul.innerHTML = list.map(item => {
      const texto = (item && typeof item === 'object') ? item.palabra : item;
      return `<li>${texto}</li>`;
    }).join('');

    ul.style.maxHeight = '264px';
    ul.style.overflowY = 'auto';
    ul.hidden = false;

  } catch (error) {
    console.error("Error al buscar sugerencias:", error);
    ul.hidden = true;
  }
});

ul.addEventListener('click', e => {
  if (e.target.tagName === 'LI') {
    input.value = e.target.textContent;
    ul.hidden = true;
    input.focus();
  }
});

document.addEventListener('click', e => {
  if (!input.contains(e.target) && !ul.contains(e.target)) {
    ul.hidden = true;
  }
});
