<?php
//Inicio de sesion
session_start();
error_reporting(E_ERROR);
//Incluimos el controlador de Usuarios
require_once '../controlador/UsuariosController.php';


//Atraves del metodo POST obtenemos los datos del formulario
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    //Obtenemos los datos del formulario
    $nombre = $_POST['nombre'];
    $passw = $_POST['passw'];
    $email = $_POST['email'];
    $rol = $_POST['rol'];

    $controller = new UsuariosController();
    //Verificamos si el correo ya esta registrado
    $checkemail = $controller->obtenerUsuarioPorEmail($email);

   //Si el correo no esta registrado, se agrega el usuario
    if ($checkemail == null) {
        $resultado = $controller->agregarUsuario($nombre, $passw, $email, $rol);
        header("Location: ../index.php");
        exit();
    }

    //Si el correo ya esta registrado, se muestra un mensaje de error
    else {
       error_log("Error de inicio de sesión para usuario: " . $usuariolog);
        $error_message = "Este correo ya esta registrado.";
    }
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/styleError.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <title>Registro</title>
</head>

<body>
    <div class="container mt-4">
        <h1>Registro</h1>
        <form action="alta_usuario.php" method="POST">
        <?php if (isset($error_message)): ?>
            <p class="error-message"><?= $error_message ?></p>
        <?php endif; ?>
            <div class="mb-3">
                <label for="nombre" class="form-label" maxlength="25">Nombre de usuario</label>
                <input type="text" class="form-control" id="nombre" name="nombre" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label" maxlength="100">Correo Electronico</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="passw" class="form-label" maxlength="255">Contraseña</label>
                <input type="password" class="form-control" id="passw" name="passw" required>
            </div>
            
            <div class="mb-3" hidden>
                <label for="rol" class="form-label">Rol</label>
                <select class="form-select" id="rol" name="rol" >
                

                    <option value="admin">Admin</option>
                
                    <option value="user" selected>User</option>
                </select>
            </div>
            <!-- Un checkbox para activar el boton atraves del onchange enabler() que se desactiva o se active -->
                <input type="checkbox" id="checkbox" onchange="enabler()">
                <label for="checkbox" >Aceptar términos y condiciones</label>

            <br>
            <br>
            <button id="button" type="submit" class="btn btn-primary" disabled>Guardar</button>
        </form>
    </div>
    <script src="../script/script.js"></script>
</body>

</html>