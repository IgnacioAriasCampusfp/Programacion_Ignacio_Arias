<?php
session_start();
if ($_SESSION['usuario'] == 'admin') { 

} else {
  header("Location: login.php");
}
require_once '../controlador/TareaController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_tarea = $_GET['id'] ?? null;

    if ($id_tarea) {
       $controller = new TareasController();
        $controller->eliminarTarea($id_tarea);
            
    
    }
}



header('Location: lista_tarea.php');
exit();
?>