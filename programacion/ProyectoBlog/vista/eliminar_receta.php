<?php
require_once '../controlador/RecetasController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_receta = $_GET['id'] ?? null;

    if ($id_receta) {
       $controller = new RecetasController();
        $controller->eliminarRecetas($id_receta);
            
    
    }
}



header('Location: lista_reectas.php');
exit();
?>