<?php
require_once '../controlador/SociosController.php';
$controller = new SociosController();
$socios = $controller->listarSocios();
?>

<!DOCTYPE html>
<html lang="es">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZwv-model-vue1T" crossorigin="anonymous" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>

<head>
  <meta charset="UTF-8">
  <title>Listado de Socios</title>
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
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle " href="" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Socios
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="lista_socios.php">Socios</a></li>
              <li><a class="dropdown-item btn-primary" href="alta_socio.php">Añadir Socios</a></li>
              <li><a class="dropdown-item btn-success" href="editar_socio.php">Editar Socios</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="?opcion=articulos" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Articulos
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="lista_eventos.php">Articulos</a></li>
              <li><a class="dropdown-item btn-primary" href="alta_eventos.php">Añadir Eventos</a></li>
              <li><a class="dropdown-item btn-success" href="editar_eventos.php">Editar Eventos</a></li>
            </ul>
          </li>


        </ul>
      </div>
    </div>
  </nav>
  <h1>Socios Registrados</h1> <br>



  <table class="table">
    <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Email</th>
        <th scope="col">Teléfono</th>
        <th scope="col">Fecha de Nacimiento</th>
        <th scope="col">Acciones</th>

      </tr>
    </thead>
    <tbody>
      <?php foreach ($socios as $socio): ?>
        <tr>
          <td scope="row"><?= $socio['id_socio'] ?></td>
          <td><?= $socio['nombre'] ?></td>
          <td><?= $socio['apellido'] ?></td>
          <td><?= $socio['email'] ?></td>
          <td><?= $socio['telefono'] ?></td>
          <td><?= $socio['fecha_nacimiento'] ?></td>
          <td>
            <button class="btn btn-danger mb-3">
              <a href="eliminar_socio.php?id=<?= $socio['id_socio'] ?>" class="text-white text-decoration-none">Eliminar</a>
            </button>

          </td>
        </tr>
      <?php endforeach; ?>

    </tbody>
  </table>

</body>

</html>