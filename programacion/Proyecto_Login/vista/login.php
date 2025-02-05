<?php
error_reporting(E_ERROR);
require_once '../controlador/UsuariosController.php';
session_start();
session_regenerate_id(true);
$controller = new UsuariosController;




if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuariolog = $_POST['username'];
    $password = $_POST['password'];
    $user = $controller->obtenerUsuarioPorNombre($usuariolog);

    // 🔍 Verificar si se está obteniendo el usuario
    error_log("Usuario obtenido: " . print_r($user, true));

    if ($usuariolog == $user['usuario'] && $password == $user['passw']) {
        $_SESSION['usuario'] = $user['rol'];
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
                <label for="username">Usuario</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Contraseña</label>
                <input type="password" id="password" name="password">
            </div>
            <button type="submit" class="login-button">Ingresar</button>
        </form>
    </div>
</body>

</html>