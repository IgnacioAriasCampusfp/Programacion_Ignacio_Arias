<?php
require_once '../controlador/ClientesController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_socio = $_GET['id'] ?? null;

    if ($id_socio) {
       $controller = new ClientesController();
        $controller->eliminarCliente($id_socio);
            
    
    }
}



header('Location: ../index.php');
exit();
?>