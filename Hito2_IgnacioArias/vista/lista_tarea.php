<?php
//Obtenemos el controlador de tareas
require_once '../controlador/TareaController.php';
//Iniciamos la sesión con un id regenativo
session_start();
session_regenerate_id(true);
//Creamos una instancia del controlador de tareas
$controller = new TareasController();
//Obtenemos el email de la sesión
$email = $_SESSION['email'];
//Obtenemos las tareas del usuario atraves de la función listarTareas
$tareas = $controller->listarTareas($email);

//Si el usuario no es admin o user lo redirigimos a la página de login
if ($_SESSION['usuario'] == 'admin' || $_SESSION['usuario'] == 'user') {
} else {
    header("Location: login.php");
}
?>

<!DOCTYPE html>
<html lang="es">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>

<head>
    <meta charset="UTF-8">
    <title>Listado de tareas</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">La wea</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <!-- Barra de navegacion para Tareas -->
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdowntareas" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Tareas
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdowntareas">
                            <li><a class="dropdown-item" href="lista_tarea.php">Tareas</a></li>
                            <li><a class="dropdown-item btn-primary" href="alta_tarea.php">Añadir Tareas</a></li>
                        </ul>
                    </li>

                </ul>

                <!-- Usuario logueado y botón de cerrar sesión alineados a la derecha -->
                <div class="d-flex ms-auto align-items-center">
                    <span class="me-3">Bienvenido, <strong><?php echo $_SESSION['nombre']; ?></strong></span>
                    <a href="logout.php" class="btn btn-danger">Cerrar sesión</a>
                </div>
            </div>
        </div>
    </nav>

    <h1>Tareas Registradas</h1> <br>



    <table class="table">
        <thead>
            <tr>
                <th scope="col">Titulo</th>
                <th scope="col" class="w-50">Descripción</th>
                <th scope="col">Estado</th>
                <th scope="col">Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php //Recorremos las tareas y las mostramos en la tabla 
            foreach ($tareas as $tarea): ?>
                <tr>
                    <td scope="row"><strong><?= $tarea['titulo'] ?></strong></td>
                    <td class="w-50"><?= $tarea['descripcion'] ?></td>
                    <td>
                        <form action="editar_tarea.php" method="POST" onchange="this.submit()">
                        <input type="hidden" name="id_tarea" value="<?= $tarea['id_tarea'] ?>">
                            <select name="estado" class="form-select">
                                <!-- Mostramos el estado de la tarea en un select -->
                                 <!-- Podemos elegir el estado de la tarea lanzaremos una funcion en JS para que lo cambie a la base de datos -->
                                <option value="completada" <?= $tarea['estado'] == 'Completada' ? 'selected' : '' ?>>Completada</option>
                                <option value="en_curso" <?= $tarea['estado'] == 'En_curso' ? 'selected' : '' ?>>En curso</option>
                                <option value="pausada" <?= $tarea['estado'] == 'Pausada' ? 'selected' : '' ?>>Pausada</option>
                                <option value="cancelada" <?= $tarea['estado'] == 'Cancelada' ? 'selected' : '' ?>>Cancelada</option>
                            </select>
                        </form>
                    </td>
                    <td>
                        <button class="btn btn-danger mb-3">
                            <a href="eliminar_tarea.php?id=<?= $tarea['id_tarea'] ?>" class="text-white text-decoration-none">Eliminar</a>
                        </button>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>


</body>

</html>