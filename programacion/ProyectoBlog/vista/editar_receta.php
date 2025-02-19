<?php
require_once '../controlador/RecetasController.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $id = $_POST['id'];
    $titulo = $_POST['titulo'];
    $descripcion = $_POST['descripcion'];

    $controller = new RecetasController();
    $resultado = $controller->editarReceta($id, $titulo, $descripcion);

    echo json_encode(["success" => $stmt->execute()]);
}
?>
