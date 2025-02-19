<?php
require_once '../config/class_conexion.php';

class Socio {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }

    public function agregarReceta($titulo, $descripcion) {
        $query = "INSERT INTO recetas (titulo, descripcion) VALUES (?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ss", $titulo, $descripcion);

        if ($stmt->execute()) {
            echo "Socio agregado con éxito.";
        } else {
            echo "Error al agregar socio: " . $stmt->error;
        }

        $stmt->close();
    }

    public function obtenerRecetas() {
        $query = "SELECT * FROM recetas";
        $resultado = $this->conexion->conexion->query($query);
        $recetas = [];
        while ($fila = $resultado->fetch_assoc()) {
            $recetas[] = $fila;
        }
        return $recetas;
    }

    public function eliminarRecetas($id_receta) {
        // Eliminar plan usando su ID para que no haya problemas con la clave foranea
        $query = "DELETE FROM recetas WHERE id_receta = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_receta);
        if ($stmt->execute()) {
            echo "cliente eliminado con éxito.";
        } else {
            echo "Error al eliminar cliente: " . $stmt->error;
        }

        $stmt->close();
    }
    public function editarReceta($id_receta, $titulo, $descripcion) {
        $query = "UPDATE recetas SET titulo = ?, descripcion = ? WHERE id_receta = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssi", $titulo, $descripcion, $id_receta);
    
        if ($stmt->execute()) {
            echo "Receta actualizada con éxito.";
        } else {
            echo "Error al actualizar la receta: " . $stmt->error;
        }
    
        $stmt->close();
    }
    
}
?>
