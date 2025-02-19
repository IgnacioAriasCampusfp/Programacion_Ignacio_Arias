<?php
require_once '../modelo/class_recetas.php';

class RecetasController {
    private $modelo;

    public function __construct() {
        $this->modelo = new Socio();
    }

    public function agregarReceta($titulo, $descripcion) {
        $this->modelo->agregarReceta($titulo, $descripcion);
    }

    public function listarRecetas() {
        return $this->modelo->obtenerRecetas();
    }

    public function eliminarRecetas($id_receta) {
        return $this->modelo->eliminarRecetas($id_receta);
    }

    public function editarReceta($id_receta, $titulo, $descripcion){
        return $this->modelo->editarReceta($id_receta, $titulo, $descripcion);
    }


}
?>
