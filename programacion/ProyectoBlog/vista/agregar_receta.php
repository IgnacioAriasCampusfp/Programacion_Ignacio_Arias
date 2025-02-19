<?php
require_once '../controlador/RecetasController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['titulo']) && isset($_GET['respuesta'])) {
    $titulo = $_GET['titulo'];
    $contenido = $_GET['respuesta'];

    $controller = new RecetasController();
    $resultado = $controller->agregarReceta($titulo, $contenido);

    header("Location: ../index.php"); // Redirige al inicio después de agregar la receta
    exit();
} else {
    echo "Error: Faltan datos para agregar la receta.";
}
?>
