<?php
session_start();

// Si el usuario es admin, lo redirigimos a la lista de tareas
if ($_SESSION['usuario'] == 'admin' || $_SESSION['usuario'] == 'user') {
    
    header("Location: vista/lista_tarea.php");
    
}// Si no, lo redirigimos al login
else {
    header("Location: vista/login.php");
}
?>

