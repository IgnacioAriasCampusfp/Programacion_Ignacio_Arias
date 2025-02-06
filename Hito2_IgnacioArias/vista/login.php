<?php
//Elige el nivel de error que deseamos ver
error_reporting(E_ERROR);
//Incluimos el controlador de usuarios
require_once '../controlador/UsuariosController.php';
//Iniciamos la sesión con un id regenativo
session_start();
session_regenerate_id(true);
//Creamos una instancia del controlador de usuarios
$controller = new UsuariosController;

//Hacemos una petición POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    //Obtenemos los datos del formulario
    $email = $_POST['email'];
    $password = $_POST['password'];
    //Obtenemos el usuario por email atraves de la función obtenerUsuarioPorEmail
    $user = $controller->obtenerUsuarioPorEmail($email);


//Si el usuario existe y la contraseña es correcta iniciamos sesión
    if ($user && $email == $user['email'] && password_verify($password, $user['passw'])) {
        //Guardamos los datos del usuario en la sesión
        $_SESSION['usuario'] = $user['rol'];
        $_SESSION['nombre'] = $user['usuario'];
        $_SESSION['email'] = $user['email'];
        //Redirigimos a la página de inicio
        header("Location: ../index.php");
        exit();
    } else {
        //Si el usuario no existe o la contraseña es incorrecta mostramos un mensaje de error
        error_log("Error de inicio de sesión para usuario: " . $usuariolog);
        $error_message = "Usuario o contraseña incorrectos.";
    }
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <title>Login</title>

</head>

<body>
    <div class="login-container">
        <h2>Iniciar Sesión</h2>
        <?php //Mostramos el mensaje de error si el usuario o la contraseña son incorrectos 
        if (isset($error_message)): ?>
            <p class="error-message"><?= $error_message ?></p>
        <?php endif; ?>
        <form action="#" method="POST">
            <div class="input-group">
                <label for="email">Correo Electronico</label>
                <input type="email" id="email" name="email">
            </div>
            <div class="input-group">
                <label for="password">Contraseña</label>
                <input type="password" id="password" name="password">
            </div>
            <button type="submit" class="login-button">Ingresar</button>
            <br>
            <br>
            <div style="text-align: center;">
                <a href="alta_usuario.php" class="login-button">Registrarse</a>
            </div>


        </form>
    </div>
</body>

</html>