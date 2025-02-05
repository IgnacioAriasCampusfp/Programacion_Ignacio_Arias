<?php
session_start();
if ($_SESSION['usuario'] == 'admin'  ) { 

} else {
  header("Location: login.php");
}
require_once '../controlador/EventosController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_evento = $_GET['id'] ?? null;

    if ($id_evento) {
       $controller = new EventosController();
        $controller->eliminarEventos($id_evento);
            
    
    }
}



header('Location: lista_eventos.php');
exit();
?>