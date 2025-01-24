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

    if (select.value === 'Deporte') {
      if (suscripcion.value === 'Mensual') {
        suscripcion.hidden = true;
        suscripcion.disable = true;
        suscripcion.value === 'Anual';
        
      } else {
        suscripcion.hidden = false;
        suscripcion.disable = false;

      }
    } else {
      suscripcion.hidden = false;
      suscripcion.disable = false;

    }
  }
}
function mostrarPaquetesExtra() {
  const paquetesExtra = document.getElementById('PaquetesExtra');
  const planBase = document.getElementById('PlanBase');
  const seleccion = planBase.options[planBase.selectedIndex].value;
  const lable = document.getElementById('PaquetesExtraL')

  if (seleccion === 'Estandar' || seleccion === 'Premium' ) {
    paquetesExtra.hidden = false;
    paquetesExtra.disabled = false;
    lable.hidden = false;
  } else {
    paquetesExtra.hidden = true;
    paquetesExtra.disabled = true;
    lable.hidden = true;

  }
}
function desactivarDuplicados() {
  const selectExtra = document.getElementById('PaquetesExtra').options;
  const select = document.getElementById('Paquetes').value;

  if (select === 'Deporte') {
    for (let i = 0; i < selectExtra.length; i++) {
      const paquete = selectExtra[i];
      if (paquete.value === 'Deporte' || 
          paquete.value === 'Deporte,Cine' || 
          paquete.value === 'Deporte,Infantil' ||
          paquete.value === 'Cine,Deporte' ||
          paquete.value === 'Infantil,Deporte'
        ) {
        paquete.disabled = true;
        paquete.hidden = true;
      } else {
        paquete.disabled = false;
        paquete.hidden = false;

      }
    }
  } else {
    for (let i = 0; i < selectExtra.length; i++) {
      selectExtra[i].disabled = false;
    }
  }
}


function globalOpciones(){
  desactivarOpciones();
  desactivarDuplicados();
}

