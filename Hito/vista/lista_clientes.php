<?php
require_once '../controlador/ClientesController.php';
$controller = new ClientesController();
$clientes = $controller->listarclientes();

// Definir los costos asociados a cada plan y paquete
$costos = [
    'PlanBase' => [
        'Basico' => 9.99,
        'Estandar' => 13.99,
        'Premium' => 17.99
    ],
    'PaquetesAdicionales' => [
        'Deporte' => 6.99,
        'Cine' => 7.99,
        'Infantil' => 4.99
    ],
    'Duracion' => [
        'Mensual' => 1,
        'Anual' => 12
    ]
];

// Función para calcular el costo total
function calcularCosto($cliente, $costos) {
    // Obtener el costo del plan base
    $costoPlanBase = $costos['PlanBase'][$cliente['PlanBase']];
    // Obtener el costo de los paquetes adicionales
    $paquetes = explode(',', $cliente['PaquetesAdicionales']);
    // Sumar el costo de cada paquete adicional
    $costoPaquetes = array_reduce($paquetes, function($carry, $item) use ($costos) {
        // Sumar el costo del paquete adicional al acumulador
        return $carry + $costos['PaquetesAdicionales'][$item];
    }, 0);
    // Obtener la duración del plan
    $duracion = $costos['Duracion'][$cliente['Duracion']];
    // Calcular el costo total
    return ($costoPlanBase + $costoPaquetes) * $duracion;
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Listado de clientes</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <!-- Barra de navegacion para los distintos archivos necesarios -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="../index.php">Hito</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownClientes" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Clientes
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownClientes">
                      <li><a class="dropdown-item" href="lista_clientes.php">Clientes</a></li>
                      <li><a class="dropdown-item" href="alta_clientes.php">Añadir clientes</a></li>
                      <li><a class="dropdown-item" href="editar_clientes.php">Editar clientes</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="container mt-5">
    <h1 class="mb-4">Clientes Registrados</h1>
    <!-- Filtro para buscar clientes por cualquier opcion -->
    <div class="input-group mb-3">
        <input type="text" class="form-control" id="nameFilter" placeholder="Filtrar por datos" oninput="filterData()">
        
    </div>
    <!-- Tabla para mostrar los clientes registrados -->
    <table class="table table-striped table-hover">
        <thead class="table-dark">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Nombre</th>
                <th scope="col">Apellido</th>
                <th scope="col">Email</th>
                <th scope="col">Plan Base</th>
                <th scope="col">Paquete Adicional</th>
                <th scope="col">Duración</th>
                <th scope="col">Costo Total</th>
                <th scope="col">Acciones</th>
            </tr>
        </thead>
        <tbody id="clientesTableBody">
            <?php foreach ($clientes as $cliente): ?>
                <tr>
                    <td scope="row"><?= $cliente['id_cliente'] ?></td>
                    <td><?= $cliente['nombre'] ?></td>
                    <td><?= $cliente['apellidos'] ?></td>
                    <td><?= $cliente['email'] ?></td>
                    <td><?= $cliente['PlanBase'] ?></td>
                    <td><?= $cliente['PaquetesAdicionales'] ?></td>
                    <td><?= $cliente['Duracion'] ?></td>
                    <td><?= calcularCosto($cliente, $costos) ?> €</td>
                    <td>
                        <a href="eliminar_cliente.php?id=<?= $cliente['id_cliente'] ?>" class="btn btn-danger btn-sm">Eliminar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="../scripts/script.js"></script>

</body>
</html>
