

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
