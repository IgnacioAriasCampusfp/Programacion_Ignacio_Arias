<?php
require_once '../config/class_conexion.php';

class Cliente {
    private $conexion;
    // Constructor de la clase
    public function __construct() {
        $this->conexion = new Conexion();
    }
    // Funcion para agregar un cliente
    public function agregarcliente($nombre, $apellidos, $correo, $Edad, $PlanBase, $PaquetesAdicionales, $Duracion) {
        // Insertar cliente
        $query = "INSERT INTO Clientes (nombre, apellidos, email, edad) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssss", $nombre, $apellidos, $correo, $Edad);
        
        if ($stmt->execute()) {
            echo "Cliente agregado con éxito.";
        } else {
            echo "Error al agregar cliente: " . $stmt->error;
        }
        // Obtener ID del cliente para insertar en la base de datos plan
        $query = "SELECT id_cliente FROM Clientes WHERE email=?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("s", $correo);  
        $stmt->execute();
        $resultado = $stmt->get_result();
    
        if ($fila = $resultado->fetch_assoc()) {
            $id_guardado = $fila['id_cliente'];
        } else {
            echo "Error al obtener el ID del cliente.";
            return;
        }
        // Insertar en base de datos plan
        $query = "INSERT INTO planes (id_cliente, PlanBase, PaquetesAdicionales, Duracion) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("isss", $id_guardado, $PlanBase, $PaquetesAdicionales, $Duracion);
        if ($stmt->execute()) {
            echo "Plan agregado con éxito.";
        } else {
            echo "Error al agregar plan: " . $stmt->error;
        }
    
        $stmt->close();
    }
    
    // Funcion para obtener todos los clientes
    public function obtenerClientes() {
        // Obtener todos los clientes
        $query = "SELECT * FROM clientes inner join planes on clientes.id_cliente = planes.id_cliente";
        $resultado = $this->conexion->conexion->query($query);
        $Clientes = [];
        while ($fila = $resultado->fetch_assoc()) {
            $Clientes[] = $fila;
        }
        // Retornar todos los clientes
        return $Clientes;
    }
    // Funcion para obtener un cliente por su ID
    public function obtenerclientePorId($id_cliente) {
        $query = "SELECT * FROM Clientes WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_cliente);
        $stmt->execute();
        $resultado = $stmt->get_result();
        return $resultado->fetch_assoc();
    }
    // Funcion para actualizar un cliente
    public function actualizarcliente($id_cliente, $nombre, $apellidos, $correo, $Edad, $PlanBase, $PaquetesAdicionales, $Duracion) {
        // Actualizar base de datos cliente
        $query = "UPDATE Clientes SET nombre = ?, apellidos = ?, email = ?, edad = ? WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssii", $nombre, $apellidos, $correo, $Edad, $id_cliente);

        if ($stmt->execute()) {
            echo "cliente actualizado con éxito.";
        } else {
            echo "Error al actualizar cliente: " . $stmt->error;
        }
        // Actualizar base de datos plan
        $query = "UPDATE planes SET PlanBase = ?, PaquetesAdicionales = ?, Duracion = ? WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssi", $PlanBase, $PaquetesAdicionales, $Duracion, $id_cliente);

        if ($stmt->execute()) {
            echo "cliente actualizado con éxito.";
        } else {
            echo "Error al actualizar cliente: " . $stmt->error;
        }

        
        $stmt->close();
    }
    // Funcion para eliminar un cliente
    public function eliminarcliente($id_cliente) {
        // Eliminar plan usando su ID para que no haya problemas con la clave foranea
        $query = "DELETE FROM planes WHERE id_cliente = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_cliente);
        if ($stmt->execute()) {
            echo "cliente eliminado con éxito.";
        } else {
            echo "Error al eliminar cliente: " . $stmt->error;
        }
        // Eliminar cliente usando su ID
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
