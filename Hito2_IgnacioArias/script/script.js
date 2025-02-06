function cambiarEstado(id_tarea, nuevo_estado) {
    const valor = new XMLHttpRequest();
    valor.open("POST", "editar_tarea.php", true);
    valor.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    valor.onreadystatechange = function() {
        if (valor.readyState === 4 && valor.status === 200) {
            console.log("Estado actualizado correctamente");
        }
    };
    valor.send("id_tarea=" + id_tarea + "&estado=" + nuevo_estado);
}

function enabler(){
    const button = document.getElementById("button");
    const check = document.getElementById("checkbox");
    button.disabled = !check.checked;
}