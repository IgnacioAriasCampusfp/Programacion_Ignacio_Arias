<?php
session_start();


require_once '../controlador/TareaController.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id_tarea'];
    $estado = $_POST['estado'];

    $controller = new TareasController();
    $resultado = $controller->actualizarTarea($id, $estado);

    header("Location: ../index.php");
    exit();
}
?>3