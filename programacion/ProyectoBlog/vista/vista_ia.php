<?php
require_once '../controlador/IaController.php';

$controller = new RecetaAIController();
$titulo = $_POST['mensaje'] ?? '';
$textorespuesta = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($titulo)) {
    $textorespuesta = $controller->generarReceta($titulo);
}
$encabezado = file_get_contents("encabezado.html");

echo $encabezado;
include "prompt_ia.php";
?>
