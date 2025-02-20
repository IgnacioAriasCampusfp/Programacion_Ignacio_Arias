
<div class="container mt-4">
    <h1 class="text-center">Recetas Registradas</h1>
    <br>
    
    <?php if (!empty($recetas)): ?>
        <div class="row">
            <?php foreach ($recetas as $receta): ?>
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title" id="titulo-<?= $receta['id_receta'] ?>">
                                <?= htmlspecialchars($receta['titulo']) ?>
                            </h5>
                            <p class="card-text" id="descripcion-<?= $receta['id_receta'] ?>">
                                <?= nl2br(htmlspecialchars($receta['descripcion'])) ?>
                            </p>
                            <button class="btn btn-warning btn-sm" onclick="mostrarFormulario(<?= $receta['id_receta'] ?>)">Editar</button>
                            <a href="eliminar_receta.php?id=<?= $receta['id_receta'] ?>" class="btn btn-danger btn-sm">Eliminar</a>
                            
                            <!-- Formulario de edición (oculto por defecto) -->
                            <div id="form-<?= $receta['id_receta'] ?>" style="display: none; margin-top: 10px;">
                                <input type="text" class="form-control mb-2" id="edit-titulo-<?= $receta['id_receta'] ?>" value="<?= htmlspecialchars($receta['titulo']) ?>">
                                <textarea class="form-control mb-2" id="edit-descripcion-<?= $receta['id_receta'] ?>"><?= htmlspecialchars($receta['descripcion']) ?></textarea>
                                <button class="btn btn-success btn-sm" onclick="guardarEdicion(<?= $receta['id_receta'] ?>)">Guardar</button>
                                <button class="btn btn-secondary btn-sm" onclick="cancelarEdicion(<?= $receta['id_receta'] ?>)">Cancelar</button>
                            </div>
                        </div>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    <?php else: ?>
        <div class="alert alert-warning text-center" role="alert">
            No hay recetas guardadas.
        </div>
    <?php endif; ?>
</div>

<script>
// Mostrar formulario de edición
function mostrarFormulario(id) {
    document.getElementById('form-' + id).style.display = 'block';
}

// Ocultar formulario de edición
function cancelarEdicion(id) {
    document.getElementById('form-' + id).style.display = 'none';
}

// Guardar cambios usando AJAX
function guardarEdicion(id) {
    var titulo = document.getElementById('edit-titulo-' + id).value;
    var descripcion = document.getElementById('edit-descripcion-' + id).value;

    $.post('editar_receta.php', { id: id, titulo: titulo, descripcion: descripcion }, function(response) {
        var data = JSON.parse(response);
        if (data.success) {
            // Actualizar visualmente sin recargar la página
            document.getElementById('titulo-' + id).innerText = titulo;
            document.getElementById('descripcion-' + id).innerText = descripcion;
            cancelarEdicion(id);
        } else {
            alert("Error al actualizar la receta.");
        }
    });
}
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
