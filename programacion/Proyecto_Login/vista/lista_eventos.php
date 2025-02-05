<?php
session_start();
if ($_SESSION['usuario'] == 'admin' ||$_SESSION['usuario'] == 'user' ) { 

} else {
  header("Location: login.php");
}
require_once '../controlador/EventosController.php';
$controller = new EventosController();
$Eventos = $controller->listarEventos();
?>

<!DOCTYPE html>
<html lang="es">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <link rel="stylesheet"href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZwv-model-vue1T"crossorigin="anonymous"/><meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"crossorigin="anonymous"></script>
        <!-- Bootstrap 5 JS (y Popper.js que es necesario para el desplegable) -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
      
<head>
    <meta charset="UTF-8">
    <title>Listado de Eventos</title>
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
                <!-- Socios -->
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownSocios" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Socios
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownSocios">
                        <li><a class="dropdown-item" href="lista_socios.php">Socios</a></li>
                        <?php if ($_SESSION['usuario'] == 'admin') { ?>
                            <li><a class="dropdown-item btn-primary" href="alta_socio.php">Añadir Socios</a></li>
                            <li><a class="dropdown-item btn-success" href="editar_socio.php">Editar Socios</a></li>
                        <?php } ?>
                    </ul>
                </li>

                <!-- Artículos -->
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownArticulos" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Eventos
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownArticulos">
                        <li><a class="dropdown-item" href="lista_eventos.php">Eventos</a></li>
                        <?php if ($_SESSION['usuario'] == 'admin') { ?>
                            <li><a class="dropdown-item btn-primary" href="alta_eventos.php">Añadir Eventos</a></li>
                            <li><a class="dropdown-item btn-success" href="editar_eventos.php">Editar Eventos</a></li>
                        <?php } ?>
                    </ul>
                </li>

                <!-- Usuarios (solo para admin) -->
                <?php if ($_SESSION['usuario'] == 'admin') { ?>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownUsuarios" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Usuarios
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownUsuarios">
                            <li><a class="dropdown-item" href="listar_usuarios.php">Usuarios</a></li>
                            <li><a class="dropdown-item btn-primary" href="alta_usuario.php">Añadir Usuarios</a></li>
                            <li><a class="dropdown-item btn-success" href="editar_usuario.php">Editar Usuarios</a></li>
                        </ul>
                    </li>
                <?php } ?>
            </ul>

            <!-- Usuario logueado y botón de cerrar sesión alineados a la derecha -->
            <div class="d-flex ms-auto align-items-center">
                <span class="me-3">Bienvenido, <strong><?php echo $_SESSION['usuario']; ?></strong></span>
                <a href="logout.php" class="btn btn-danger">Cerrar sesión</a>
            </div>
        </div>
    </div>
</nav>

<h1>Eventos Registrados</h1>    <br>
<table class="table">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Evento</th>
      <th scope="col">Fecha</th>
      <th scope="col">Lugar</th>
      <th scope="col">Acciones</th>



    </tr>
  </thead>
  <tbody>
  <?php foreach ($Eventos as $socio): ?>
            <tr>
                <td scope="row"><?= $socio['id_evento'] ?></td>
                <td><?= $socio['nombre_evento'] ?></td>
                <td><?= $socio['fecha'] ?></td>
                <td><?= $socio['lugar'] ?></td>

                <td>  
                  <button class="btn btn-danger mb-3" ><a href="eliminar_eventos.php?id=<?= $socio['id_evento'] ?>">Eliminar</a></button>
              
                </td>
            </tr>
        <?php endforeach; ?>
    
  </tbody>
</table>

</body>
</html>
