<?php
//Inicio de sesion
session_start();
require_once '../controlador/TareaController.php';
//Obtenemos otra ves de la lista_tareas.php el id de la tarea y el estado que este es llamado atraves de un JS
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $id = $_POST['id_tarea'];
    $estado = $_POST['estado'];

    $controller = new TareasController();
    //Llamamos a la funcion actualizarTarea del controlador
    $resultado = $controller->actualizarTarea($id, $estado);

    //Si se actualiza la tarea redirigimos a la lista de tareas
    header("Location: ../index.php");
    exit();
}
?>3