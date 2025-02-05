<?php
session_start();

require_once '../controlador/UsuariosController.php';

if ($_SESSION['usuario'] == 'admin' ) { 

} else {
  header("Location: login.php");
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = $_POST['id'];
    $nombre = $_POST['nombre'];
    $passw = $_POST['passw'];
    $rol = $_POST['rol'];

    
    $controller = new UsuariosController();
    $resultado = $controller->actualizarUsuario($id, $nombre, $passw, $rol);
    
    
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
    <title>Editar Usuario</title>
</head>
<body>
    <div class="container mt-4">
        <h1>Editar Usuario</h1>
        <form action="editar_usuario.php" method="POST">
            <div class="mb-3">
                <label for="id" class="form-label">ID</label>
                <input type="text" class="form-control" id="id" name="id" required>
            </div>
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" class="form-control" id="nombre" name="nombre" required>
            </div>
            <div class="mb-3">
                <label for="passw" class="form-label">passw</label>
                <input type="password" class="form-control" id="passw" name="passw" required>
            </div>
            <div class="mb-3">
                <label for="rol" class="form-label">Rol</label>
                <select class="form-select" id="rol" name="rol" required>
                    <option value="admin">Admin</option>
                    <option value="user">User</option>
                </select>
            </div>
          
            <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
    </div>
</body>
</html>

