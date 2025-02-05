<?php
session_start();
if ($_SESSION['usuario'] == 'admin' ) { 

} else {
  header("Location: login.php");
}
require_once '../controlador/UsuariosController.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id_usuario = $_GET['id'] ?? null;

    if ($id_evento) {
       $controller = new UsuariosController();
        $controller->eliminarUsuario($id_usuario);
            
    
    }
}



header('Location: lista_usuarios.php');
exit();
?>