<?php
require_once '../config/class_conexion.php';

class Tarea {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }
    //Metodo para agregar un usuario atraves de los datos a la base de datos
    public function agregarTarea($email, $titulo, $descripcion, $estado) {
        //Preparamos la consulta para agregar un usuario
        $query = "INSERT INTO Tareas (email, titulo, descripcion, estado) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssss", $email, $titulo, $descripcion, $estado);
        //Si la consulta se ejecuta correctamente, se muestra un mensaje de exito
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

    //Funcion para actualizar un usuario atraves de los parametros
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
    //Funcion para eliminar un usuario atraves del id
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
