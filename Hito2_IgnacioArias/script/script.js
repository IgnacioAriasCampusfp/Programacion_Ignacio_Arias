
// Función para cambiar el estado de una tarea
function cambiarEstado(id_tarea, nuevo_estado) {
    // Crear un objeto XMLHttpRequest para hacer la petición
    const valor = new XMLHttpRequest();
    //Abrimos atraves de un metodo POST la url de editar_tarea.php y le pasamos los parametros id_tarea y estado a editar_tarea.php
    valor.open("POST", "editar_tarea.php", true);
    //Establecemos el tipo de contenido de la cabecera
    valor.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //Enviamos la petición con los parametros id_tarea y estado
    valor.send("id_tarea=" + id_tarea + "&estado=" + nuevo_estado);
}

//Función para habilitar el botón de enviar
function enabler(){
    //Obtenemos los elementos del documento alta_usuario.php
    const button = document.getElementById("button");
    const check = document.getElementById("checkbox");
    //Si el checkbox está marcado, el botón se habilita
    button.disabled = !check.checked;
}