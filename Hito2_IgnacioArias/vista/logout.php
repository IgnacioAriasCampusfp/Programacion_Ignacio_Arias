<?php
// Obtenemos los datos de la sesión
session_start();
// Eliminamos las variables de la sesión
session_unset();
// Destruimos la sesión
session_destroy();
//Volvemos a la página de login
header("Location: login.php");
?>
