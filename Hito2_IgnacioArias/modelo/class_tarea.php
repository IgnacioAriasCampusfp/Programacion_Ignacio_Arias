<?php
require_once '../config/class_conexion.php';

class Tarea {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }

    public function agregarTarea($email, $titulo, $descripcion, $estado) {
        $query = "INSERT INTO Tareas (email, titulo, descripcion, estado) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssss", $email, $titulo, $descripcion, $estado);

        if ($stmt->execute()) {
            echo "Tarea agregado con éxito.";
        } else {
            echo "Error al agregar Tarea: " . $stmt->error;
        }

        $stmt->close();
    }

    public function obtenerTareasPorEmail($email) {
        $query = "SELECT * FROM tareas where email = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $resultado = $stmt->get_result();
        $Tareas = [];
        while ($fila = $resultado->fetch_assoc()) {
            $Tareas[] = $fila;
        }
        return $Tareas;
    }

    public function obtenerTareaPorId($id_Tarea) {
        $query = "SELECT * FROM Tareas WHERE id_Tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_Tarea);
        $stmt->execute();
        $resultado = $stmt->get_result();
        return $resultado->fetch_assoc();
    }

    public function actualizarTarea($id_Tarea, $estado) {
        $query = "UPDATE tareas SET estado = ? WHERE id_tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("si", $estado, $id_Tarea);

        if ($stmt->execute()) {
            echo "Tarea actualizado con éxito.";
        } else {
            echo "Error al actualizar Tarea: " . $stmt->error;
        }

        $stmt->close();
    }

    public function eliminarTarea($id_Tarea) {
        $query = "DELETE FROM Tareas WHERE id_tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_Tarea);

        if ($stmt->execute()) {
            echo "Tarea eliminado con éxito.";
        } else {
            echo "Error al eliminar Tarea: " . $stmt->error;
        }

        $stmt->close();
    }
}
?>
