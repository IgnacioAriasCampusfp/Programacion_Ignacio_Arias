<?php
require_once 'controlador/IaController.php';

$controller = new RecetaAIController();
$titulo = $_POST['mensaje'] ?? '';
$textorespuesta = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($titulo)) {
    $textorespuesta = $controller->generarReceta($titulo);
}
?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cooking Mama</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Cooking Mama</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="index.php">Inicio</a></li>
                    <li class="nav-item"><a class="nav-link" href="vista/lista_recetas.php">Recetas</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-5 text-center">
        <h1>Cocina con IA</h1>

        <?php if (!empty($textorespuesta)) : ?>
            <div class='respuesta'>
                <strong>Respuesta:</strong>
                <p><?php echo nl2br(htmlspecialchars($textorespuesta)); ?></p>
            </div>
            <a href="vista/agregar_receta.php?titulo=<?php echo urlencode($titulo); ?>&respuesta=<?php echo urlencode($textorespuesta); ?>" class="btn btn-success mt-3">Guardar Receta</a>
        <?php endif; ?>

        <form method="POST" class="mt-4">
            <div class="mb-3">
                <textarea name="mensaje" class="form-control" placeholder="Escribe qué receta quieres realizar..." rows="4"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Enviar</button>
        </form>
    </div>
    <br>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
