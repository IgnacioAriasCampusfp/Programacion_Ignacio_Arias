<?php
require_once '../config/class_conexion.php';

class Eventos {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }

    public function agregarEvento($evento, $fecha, $lugar) {
        $query = "INSERT INTO eventos (nombre_evento, fecha, lugar) VALUES (?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sss", $evento, $fecha, $lugar);

        if ($stmt->execute()) {
            echo "Eventos agregado con éxito.";
        } else {
            echo "Error al agregar Eventos: " . $stmt->error;
        }

        $stmt->close();
    }

    public function obtenerEventos() {
        $query = "SELECT * FROM eventos";
        $resultado = $this->conexion->conexion->query($query);
        $eventos = [];
        while ($fila = $resultado->fetch_assoc()) {
            $eventos[] = $fila;
        }
        return $eventos;
    }

    public function obtenerEventosPorId($id_eventos) {
        $query = "SELECT * FROM eventos WHERE id_evento = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_eventos);
        $stmt->execute();
        $resultado = $stmt->get_result();
        return $resultado->fetch_assoc();
    }

    public function actualizarEventos($id_eventos, $evento, $fecha, $lugar) {
        $query = "UPDATE eventos SET nombre_evento = ?, fecha = ?, lugar = ? WHERE id_evento = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssi", $evento, $fecha, $lugar, $id_eventos);

        if ($stmt->execute()) {
            echo "Eventos actualizado con éxito.";
        } else {
            echo "Error al actualizar Eventos: " . $stmt->error;
        }

        $stmt->close();
    }

    public function eliminarEventos($id_eventos) {
        $query = "DELETE FROM eventos WHERE id_evento = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_eventos);

        if ($stmt->execute()) {
            echo "Eventos eliminado con éxito.";
        } else {
            echo "Error al eliminar Eventos: " . $stmt->error;
        }

        $stmt->close();
    }
}
?>
