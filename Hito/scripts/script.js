// Buscar los elementos del archivo HTML ya sea alta o editar.
// Se busca el elemento por su id y se guarda en una variable.
const edad_ = document.getElementById('edad');
const paquetes = document.querySelectorAll('select[name="Paquetes"] option');
const paquetesExtra = document.getElementById('PaquetesExtra');
const lable = document.getElementById('PaquetesExtraL');
const planBase = document.getElementById('PlanBase');

// Se agrega un evento al elemento edad_ para que cuando se escriba algo en el input se ejecute la función.
edad_.addEventListener('input', () => {
  const edad = parseInt(edad_.value, 10);

  // Se recorre el array de paquetes y se verifica si la edad es menor a 18 años.
  if (edad < 18) {
    paquetes.forEach(paquete => {
      // Si la edad es menor a 18 años solo mostramos el paquete Infantil.
      if (paquete.value === 'Infantil') {
        paquete.hidden = false;
        paquetesExtra.hidden = true;
        paquetesExtra.value = 'paqueteExtra';
        lable.hidden = true;
      } else {
        paquete.hidden = true;
      }
    });
  } else {
    // Si la edad es mayor o igual a 18 años mostramos todos los paquetes.
    paquetes.forEach(paquete => paquete.hidden = false);
    mostrarPaquetesExtra(); // Llamar a la función para verificar el PlanBase
  }
});

// En esta función se verifica que si el Plan Base es Estandar o Premium se muestren los paquetes extra.
function mostrarPaquetesExtra() {
  const seleccion = planBase.options[planBase.selectedIndex].value;
  const edad = parseInt(edad_.value, 10);

  // Si la edad es mayor o igual a 18 años y el plan base es Estandar o Premium se muestran los paquetes extra.
  if (edad >= 18 && (seleccion === 'Estandar' || seleccion === 'Premium')) {
    paquetesExtra.hidden = false;
    paquetesExtra.disabled = false;
    lable.hidden = false;
  } else {
    paquetesExtra.hidden = true;
    paquetesExtra.disabled = true;
    lable.hidden = true;
    paquetesExtra.value = 'paqueteExtra'; // Cambiar el valor cuando se oculta
  }
}

// Creamos una función para desactivar Mensual si seleccionamos un paquete ya sea de los paquetes normales
// o de los paquetes extra que sea deporte.
function desactivarOpciones() {
  const select = document.getElementById('Paquetes');
  const selectExtra = document.getElementById('PaquetesExtra');
  const suscripciones = document.getElementById('Suscripciones').options;

  for (let i = 0; i < suscripciones.length; i++) {
    const suscripcion = suscripciones[i];
    // Si el paquete seleccionado es Deporte se desactiva la opción Mensual.
    if ((select.value && select.value.includes('Deporte')) || 
        (selectExtra.value && selectExtra.value.includes('Deporte'))) {
      if (suscripcion.value === 'Mensual') {
        suscripcion.hidden = true;
        suscripcion.disabled = true;
        suscripcion.selected = false;
        // Si la suscripción es Mensual se cambia a Anual.
      } else if (suscripcion.value === 'Anual') {
        suscripcion.selected = true;
      }
    } else {
      suscripcion.hidden = false;
      suscripcion.disabled = false;
    }
  }

  // Establecer el valor de Suscripciones a 'Anual' si se selecciona un paquete que contiene 'Deporte'
  if ((select.value && select.value.includes('Deporte')) || 
      (selectExtra.value && selectExtra.value.includes('Deporte'))) {
    document.getElementById('Suscripciones').value = 'Anual';
  }
}

// Esta función se encarga de desactivar los paquetes duplicados.
function desactivarDuplicados() {
  const selectExtra = document.getElementById('PaquetesExtra').options;
  const select = document.getElementById('Paquetes').value;

  // Si el valor seleccionado en 'select' es Deporte, Cine o Infantil se desactivan los paquetes que contengan estos mismos.
  for (let i = 0; i < selectExtra.length; i++) {
    const paquete = selectExtra[i];
    if (select === 'Deporte' && (paquete.value === 'Deporte' || paquete.value.includes('Deporte'))) {
      paquete.disabled = true;
      paquete.hidden = true;
    } else if (select === 'Cine' && (paquete.value === 'Cine' || paquete.value.includes('Cine'))) {
      paquete.disabled = true;
      paquete.hidden = true;
    } else if (select === 'Infantil' && (paquete.value === 'Infantil' || paquete.value.includes('Infantil'))) {
      paquete.disabled = true;
      paquete.hidden = true;
    } else {
      paquete.disabled = false;
      paquete.hidden = false;
    }
  }
}

//Esta funcion se encarga de calcular el total de la suscripción.
function calcularTotal() {
  const planBase = document.getElementById('PlanBase').value;
  const paqueteAdicional = document.getElementById('Paquetes').value;
  const paqueteAdicionalExtra = document.getElementById('PaquetesExtra').value;
  const suscripcion = document.getElementById('Suscripciones').value;

  //Precios de los planes y paquetes.
  const precios = {
    //Planes Bases de la suscripción
    'Basico': 9.99,
    'Estandar': 13.99,
    'Premium': 17.99,
    //Paquetes Adicionales
    'Deporte': 6.99,
    'Cine': 7.99,
    'Infantil': 4.99,
    //Paquetes Adicionales Extra
    'Deporte,Cine': 14.98,
    'Cine,Infantil': 12.98,
    'Infantil,Deporte': 11.98,
    //Aqui no se selecciona nada 
    'paqueteExtra': 0 
  };
//Se calcula el total de la suscripción.
  let total = (precios[planBase] || 0) + (precios[paqueteAdicional] || 0) + (precios[paqueteAdicionalExtra] || 0);
//Si la suscripción es Anual se multiplica por 12.
  if (suscripcion === 'Anual') {
    total *= 12;
  }
//Se muestra el total en el html.
  document.getElementById('total').innerText = `Total: €${total.toFixed(2)}`;
}
//Se agrega un evento a los elementos para que cuando se seleccione algo se ejecute la función.
document.getElementById('PlanBase').addEventListener('change', calcularTotal);
document.getElementById('Paquetes').addEventListener('change', calcularTotal);
document.getElementById('PaquetesExtra').addEventListener('change', calcularTotal);
document.getElementById('Suscripciones').addEventListener('change', calcularTotal);


//Esta función se encarga de ejecutar dos de las funciones anteriores.
function globalOpciones(){
  desactivarOpciones();
  desactivarDuplicados();
}

// Función para filtrar los datos según los valores en los inputs
function filterData() {
  const nameFilter = document.getElementById('nameFilter').value.toLowerCase();
  const rows = document.querySelectorAll('#clientesTableBody tr');

  rows.forEach(row => {
    const nombre = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
    const apellidos = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
    const email = row.querySelector('td:nth-child(4)').textContent.toLowerCase();
    const planBase = row.querySelector('td:nth-child(5)').textContent.toLowerCase();
    const paquetesAdicionales = row.querySelector('td:nth-child(6)').textContent.toLowerCase();
    const duracion = row.querySelector('td:nth-child(7)').textContent.toLowerCase();

    if (
      nombre.includes(nameFilter) ||
      apellidos.includes(nameFilter) ||
      email.includes(nameFilter) ||
      planBase.includes(nameFilter) ||
      paquetesAdicionales.includes(nameFilter) ||
      duracion.includes(nameFilter)
    ) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}