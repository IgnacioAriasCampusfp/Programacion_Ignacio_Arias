<?php
session_start();
if ($_SESSION['usuario'] == 'admin') { 

} else {
  header("Location: login.php");
}
require_once '../controlador/EventosController.php';


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id'];
    $evento = $_POST['evento'];
    $fecha = $_POST['fecha'];
    $lugar = $_POST['lugar'];

    
    $controller = new EventosController();
    $resultado = $controller->actualizarEventos($id, $evento, $fecha, $lugar);
    
    
    header("Location: ../index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <title>Editar Evento</title>
</head>
<body>
    <div class="container mt-4">
        <h1>Editar Evento</h1>
        <form action="editar_eventos.php" method="POST">
            <div class="mb-3">
                <label for="id" class="form-label">ID</label>
                <input type="text" class="form-control" id="id" name="id" required>
            </div>
            <div class="mb-3">
                <label for="evento" class="form-label">evento</label>
                <input type="text" class="form-control" id="evento" name="evento" required>
            </div>
            <div class="mb-3">
                <label for="fecha" class="form-label">fecha</label>
                <input type="date" class="form-control" id="fecha" name="fecha" required>
            </div>
            <div class="mb-3">
                <label for="text" class="form-label">lugar</label>
                <input type="text" class="form-control" id="lugar" name="lugar" required>
            </div>

            <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
    </div>
</body>
</html>

