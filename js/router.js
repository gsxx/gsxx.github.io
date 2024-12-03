// router.js

let ROM_FILENAME = ""; // Declarar la variable ROM_FILENAME

window.addEventListener("DOMContentLoaded", function() {
  // Obtener la ruta actual
  const path = window.location.pathname;

  // Extraer el nombre del archivo desde la ruta
  ROM_FILENAME = path.substring(path.lastIndexOf('/') + 1);
});

// Exportar la variable ROM_FILENAME
export default { ROM_FILENAME };
