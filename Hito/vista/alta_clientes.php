<?php
require_once '../controlador/ClientesController.php';




if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Se obtienen los datos del formulario
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $correo = $_POST['correo'];
    $Edad = $_POST['edad'];
    $PlanBase = $_POST['PlanBase'];
    $PaquetesAdicionales = $_POST['Paquetes'];
    $PaquetesAdicionalesExtra = $_POST['PaquetesExtra'];
    $PaqueteF = $PaquetesAdicionales . "," . $PaquetesAdicionalesExtra;
    $Duracion = $_POST['Suscripciones'];
    $precio = $_POST['precio'];
    $controller = new ClientesController();
    // Dependiendo de la selección del usuario, se agrega el cliente con los paquetes adicionales extra o no
    if($PaquetesAdicionalesExtra=='paqueteExtra'){
        $resultado = $controller->agregarCliente($nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion,$precio);
    }else{
        $resultado = $controller->agregarCliente($nombre,$apellidos, $correo, $Edad,$PlanBase,$PaqueteF,$Duracion,$precio);
    }
   
    header("Location: ../index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <title>Añadir Cliente</title>
    
    
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
    <h1 class="mb-4">Añadir Cliente</h1>
    <!-- Formulario para añadir un cliente -->
    <form action="alta_clientes.php" method="POST" class="row g-3">
        <div class="col-md-6">
            <label for="nombre" class="form-label">Nombre</label>
            <input type="text" class="form-control" id="nombre" name="nombre" required>
        </div>
        <div class="col-md-6">
            <label for="apellidos" class="form-label">Apellidos</label>
            <input type="text" class="form-control" id="apellidos" name="apellidos" required>
        </div>
        <div class="col-md-6">
            <label for="correo" class="form-label">Correo</label>
            <input type="email" class="form-control" id="correo" name="correo" required>
        </div>
        <div class="col-md-6">
            <label for="edad" class="form-label">Edad</label>
            <input type="number" class="form-control" id="edad" name="edad" required>
        </div>
        <!-- Seleccion de los planes base, paquetes adicionales y tipo de suscripcion usando funciones JS para cambiar las variables-->
        <div class="col-md-6">
            <label for="PlanBase" class="form-label">Plan Base</label>
            <select class="form-select" id="PlanBase" name="PlanBase" onchange="mostrarPaquetesExtra()" required>
                <option value="" disabled selected>Plan Base</option>
                <option value="Basico">Basico (1 dispositivo)</option>
                <option value="Estandar">Estandar (2 dispositivo)</option>
                <option value="Premium">Premium (4 dispositivo)</option>
            </select>
        </div>
        <div class="col-md-6">
            <label for="Paquetes" class="form-label">Paquetes Adicionales</label>
            <select name="Paquetes" class="form-select" id="Paquetes" onchange="globalOpciones()" required>
                <option value="" disabled selected>Paquetes Adicionales</option>
                <option id="Deporte" value="Deporte">Deporte</option>
                <option value="Cine">Cine</option>
                <option value="Infantil">Infantil</option>
            </select>
        </div>
        <div class="col-md-6" >
            <label for="PaquetesExtra" id="PaquetesExtraL" class="form-label" hidden>Paquete adicional extra</label>
            <select name="PaquetesExtra" class="form-select" id="PaquetesExtra" hidden disabled onchange="desactivarOpciones()" >
                <option selected value="paqueteExtra">Paquetes Adicionales Extra</option>
                <option value="Deporte">Deporte</option>
                <option value="Deporte,Cine">Deporte,Cine</option>
                <option value="Cine">Cine</option>
                <option value="Cine,Infantil">Cine,Infantil</option>
                <option value="Infantil">Infantil</option>
                <option value="Infantil,Deporte">Infantil,Deporte</option>
            </select>
        </div>
        <div class="col-md-6">
            <label for="Suscripciones" class="form-label">Tipo de Suscripción</label>
            <select name="Suscripciones" class="form-select" id="Suscripciones" required>
                <option value="" selected disabled>Tipo de Suscripción</option>
                <option value="Mensual">Mensual</option>
                <option value="Anual">Anual</option>
            </select>
        </div>
        <!-- Mostrar precio total de la suscripcion -->
        <div class="col-12">
            <div id="total">Total: €0.00</div>
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Guardar</button>
        </div>
    </form>
    <script src="../scripts/script.js"></script>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
