<?php
error_reporting(E_ERROR);
require_once '../controlador/UsuariosController.php';
session_start();
session_regenerate_id(true);
$controller = new UsuariosController;


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $user = $controller->obtenerUsuarioPorEmail($email);



    if ($user && $email == $user['email'] && password_verify($password, $user['passw'])) {
        $_SESSION['usuario'] = $user['rol'];
        $_SESSION['nombre'] = $user['usuario'];
        $_SESSION['email'] = $user['email'];
        header("Location: ../index.php");
        exit();
    } else {
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
        <?php if (isset($error_message)): ?>
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