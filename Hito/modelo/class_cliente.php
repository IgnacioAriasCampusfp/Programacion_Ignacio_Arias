<?php
require_once '../config/class_conexion.php';

class Cliente {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }

    public function agregarcliente($nombre, $apellido, $email, $telefono, $fecha_nacimiento) {
        $query = "INSERT INTO Clientes (nombre, apellido, email, telefono, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssss", $nombre, $apellido, $email, $telefono, $fecha_nacimiento);

        if ($stmt->execute()) {
            echo "cliente agregado con éxito.";
        } else {
            echo "Error al agregar cliente: " . $stmt->error;
        }

        $stmt->close();
    }

    public function obtenerClientes() {
        $query = "SELECT * FROM clientes inner join planes on clientes.id_cliente = planes.id_cliente";
        $resultado = $this->conexion->conexion->query($query);
        $Clientes = [];
        while ($fila = $resultado->fetch_assoc()) {
            $Clientes[] = $fila;
        }
        return $Clientes;
    }

    public function obtenerclientePorId($id_cliente) {
        $query = "SELECT * FROM Clientes WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_cliente);
        $stmt->execute();
        $resultado = $stmt->get_result();
        return $resultado->fetch_assoc();
    }

    public function actualizarcliente($id_cliente, $nombre, $apellido, $email, $telefono, $fecha_nacimiento) {
        $query = "UPDATE Clientes SET nombre = ?, apellido = ?, email = ?, telefono = ?, fecha_nacimiento = ? WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssssi", $nombre, $apellido, $email, $telefono, $fecha_nacimiento, $id_cliente);

        if ($stmt->execute()) {
            echo "cliente actualizado con éxito.";
        } else {
            echo "Error al actualizar cliente: " . $stmt->error;
        }

        $stmt->close();
    }

    public function eliminarcliente($id_cliente) {
        $query = "DELETE FROM planes WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_cliente);
        if ($stmt->execute()) {
            echo "cliente eliminado con éxito.";
        } else {
            echo "Error al eliminar cliente: " . $stmt->error;
        }
        $query = "DELETE FROM Clientes WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_cliente);

        if ($stmt->execute()) {
            echo "cliente eliminado con éxito.";
        } else {
            echo "Error al eliminar cliente: " . $stmt->error;
        }

        $stmt->close();
    }
}
?>
