<?php
require_once '../controlador/RecetasController.php';

$controller = new RecetasController();
$recetas = $controller->listarRecetas(); 

// Cargar el encabezado
$encabezado = file_get_contents("encabezado.html");

echo $encabezado;
    
// Incluir lista.php y pasarle los datos de recetas
include "lista.php"; 
?>
