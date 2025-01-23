<?php
require_once '../controlador/ClientesController.php';



if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $correo = $_POST['correo'];
    $Edad = $_POST['edad'];
    $PlanBase = $_POST['PlanBase'];
    $PaquetesAdicionales = $_POST['Paquetes'];
    $Duracion = $_POST['Suscripciones'];
    $controller = new ClientesController();
    $resultado = $controller->agregarCliente($nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion);
   
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
    <title>Añadir Cliente</title>
</head>
<body>
    <div class="container mt-4">
        <h1>Añadir Cliente</h1>
        <form action="alta_clientes.php" method="POST">
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" class="form-control" id="nombre" name="nombre" required>
            </div>
            <div class="mb-3">
                <label for="apellidos" class="form-label">Apellidos</label>
                <input type="text" class="form-control" id="apellidos" name="apellidos" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Correo</label>
                <input type="email" class="form-control" id="correo" name="correo" required>
            </div>
            <div class="mb-3">
                <label for="edad" class="form-label">Edad</label>
                <input type="text" class="form-control" id="edad" name="edad" required>
            </div>
            <div class="form-floating">
                <select class="form-select" id="PlanBase" name="PlanBase" aria-label="Floating label select example" required>
                    <option selected>Plan Base</option>
                    <option value="Basico">Basico (1 dispositivo)</option>
                    <option value="Estandar">Estandar (2 dispositivo)</option>
                    <option value="Premium">Premium (4 dispositivo)</option>
                </select>
                <label for="floatingSelect">Works with selects</label>
            </div>
            <br>
            <div class="form-floating">
            <select name="Paquetes" class="form-select" id="Paquetes" onchange="desactivarOpciones()" aria-label="Floating label select example" required>
                <option selected >Paquetes Adicionales</option>
                <option id="Deporte" value="Deporte">Deporte</option>
                <option value="Cine">Cine</option>
                <option value="Infantil">Infantil</option>
                </select>
            <label for="Paquetes"><b>Paquete adicional</b></label>
            </div>
            <br>
            <div class="form-floating" id="suscripciones-container">
                    <select name="Suscripciones" class="form-select" id="Suscripciones" aria-label="Floating label select example" required>
                    <option selected>Tipo de Suscripción</option>
                    <option value="Mensual">Mensual</option>
                    <option value="Anual">Anual</option>
                    </select>
                <label for="Suscripciones"><b>Tipo de Suscripción</b></label>
                
            </div>
        <br>
        <button type="submit" class="btn btn-primary">Guardar</button>
    <script src="../scripts/script.js"></script>
</body>
</html>
