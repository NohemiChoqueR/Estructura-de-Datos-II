document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("buscarInput");
  const lista = document.getElementById("listaContactos").getElementsByTagName("li");

  input.addEventListener("keyup", function () {
    const valor = input.value.toLowerCase();

    for (let i = 0; i < lista.length; i++) {
      const texto = lista[i].innerText.toLowerCase();
      lista[i].style.display = texto.includes(valor) ? "" : "none";
    }
  });
});
