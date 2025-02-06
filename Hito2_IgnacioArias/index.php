<?php
session_start();


if ($_SESSION['usuario'] == 'admin') {
    
    header("Location: vista/lista_tarea.php");
}elseif ($_SESSION['usuario'] == 'user') {
    header("Location: vista/lista_tarea.php");
}else {
    header("Location: vista/login.php");
}
?>

