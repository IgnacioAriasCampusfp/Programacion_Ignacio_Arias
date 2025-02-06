<?php
//Iniciamos la sesión
session_start();
require_once '../controlador/TareaController.php';
//Si el usuario no es admin lo redirigimos a la página de login
if ($_SESSION['usuario'] == 'admin') { 
} else {
  header("Location: login.php");
}

//Miramos si la petición es GET
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  //Obtenemos el id de la tarea
    $id_tarea = $_GET['id'] ?? null;
    //Si el id de la tarea no es nulo
    if ($id_tarea) {
       $controller = new TareasController();
       //Eliminamos la tarea atraves de la función eliminarTarea
        $controller->eliminarTarea($id_tarea);
            
    
    }
}


//Redirigimos a la página de lista de tareas
header('Location: lista_tarea.php');
exit();
?>