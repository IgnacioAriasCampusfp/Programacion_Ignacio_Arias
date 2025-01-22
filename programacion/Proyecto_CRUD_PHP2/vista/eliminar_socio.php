<?php
require_once '../controlador/SociosController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_socio = $_GET['id'] ?? null;

    if ($id_socio) {
       $controller = new SociosController();
        $controller->eliminarSocio($id_socio);
            
    
    }
}



header('Location: lista_socios.php');
exit();
?>