const edad_ = document.getElementById('edad');
const paquetes = document.querySelectorAll('select[name="Paquetes"] option');

edad_.addEventListener('input', () => {
  const edad = parseInt(edad_.value, 10);

 
  if (edad < 18) {
    paquetes.forEach(paquete => {
      if (paquete.value === 'Infantil') {
        paquete.hidden = false;
      } else {
        paquete.hidden = true;
      }
    });
  } else {
    paquetes.forEach(paquete => paquete.hidden = false);
  }
});

function desactivarOpciones() {
  const select = document.getElementById('Paquetes');
  const suscripciones = document.getElementById('Suscripciones').options;

  for (let i = 0; i < suscripciones.length; i++) {
    const suscripcion = suscripciones[i];

    if (suscripcion.value === 'Mensual') {
      if (select.value === 'Deporte') {
        suscripcion.hidden = true;
      } else {
        suscripcion.hidden = false;
      }
    } else {
      suscripcion.hidden = false;
    }
  }
}


