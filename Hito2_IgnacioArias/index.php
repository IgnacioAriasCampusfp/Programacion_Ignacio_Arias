<?php
session_start();


if ($_SESSION['usuario'] == 'admin') {
    
    header("Location: vista/lista_socios.php");
}elseif ($_SESSION['usuario'] == 'user') {
    header("Location: vista/lista_eventos.php");
}else {
    header("Location: vista/login.php");
}
?>

