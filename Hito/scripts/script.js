const edad_ = document.getElementById('edad');
const opciones = document.querySelectorAll('select[name="opciones"] option');//getElementsByName('opciones');
edad_.addEventListener('input', () => {
  const age = parseInt(edad_.value, 10);

  if (age < 18) {
    opciones.forEach(opcion => {
      if (opcion.value === 'opcion2') {
        opcion.disabled = false;
        alert(opcion);

      } else {
        opcion.disabled = true;
      }
    });
  } else {
    opciones.forEach(opcion => opcion.disabled = false);
  }
});