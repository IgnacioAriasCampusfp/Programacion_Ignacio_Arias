<?php
//Iniciamos sesión
session_start();
require_once '../controlador/TareaController.php';
//Si el usuario es admin o user, se muestra alta_tarea.php
if ($_SESSION['usuario'] == 'admin' || $_SESSION['usuario'] == 'user') {
} //Si no, se redirige a login.php
else {
    header("Location: login.php");
}

//Atraves del metodo POST obtenemos los datos del formulario
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    //Obtenemos los datos del formulario
    $titulo = $_POST['titulo'];
    $descripcion = $_POST['descripcion'];
    //Obtenemos el email del usuario a traves del usuario logueado
    $email = $_SESSION['email'];
    //Obtenemos el estado de la tarea
    $estado = $_POST['estado'];
    $controller = new TareasController();
    //Agregamos la tarea atraves del metodo agregarTarea
    $resultado = $controller->agregarTarea($email, $titulo, $descripcion, $estado);

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
    <title>Añadir Tarea</title>
</head>

<body>
    <div class="container mt-4">
        <h1>Añadir Tarea</h1>
        <form action="alta_tarea.php" method="POST">
            <div class="mb-3">
                <label for="titulo" class="form-label" maxlength="25">Titulo</label>
                <input type="text" class="form-control" id="titulo" name="titulo" required>
            </div>
            <div class="mb-3">
                <label for="descripcion" class="form-label">Descripción</label>
                <textarea class="form-control" id="descripcion" name="descripcion" rows="4" maxlength="255" required></textarea>
            </div>
            <label for="estado">Selecciona el estado:</label>
            <select id="estado" name="estado">
                <option value="Completada">Completada</option>
                <option value="En_curso">En curso</option>
                <option value="Pausada">Pausada</option>
                <option value="Cancelada">Cancelada</option>
            </select>
            <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
    </div>
</body>

</html>