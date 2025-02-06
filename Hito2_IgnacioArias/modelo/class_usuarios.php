<?php
require_once '../config/class_conexion.php';

class Usuario
{
    private $conexion;

    public function __construct()
    {
        $this->conexion = new Conexion();
    }

    public function agregarUsuario($usuario, $contraseña, $rol)
    {
        $query = "INSERT INTO usuarios (usuario, passw, rol) VALUES (?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sss", $usuario, $contraseña, $rol);

        if ($stmt->execute()) {
            echo "Usuario agregado con éxito.";
        } else {
            echo "Error al agregar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }

    public function obtenerUsuarios()
    {
        $query = "SELECT * FROM usuarios";
        $resultado = $this->conexion->conexion->query($query);
        $Usuarios = [];
        while ($fila = $resultado->fetch_assoc()) {
            $Usuarios[] = $fila;
        }
        return $Usuarios;
    }

    public function obtenerUsuarioPorNombre($nombre)
    {
        $query = "SELECT * FROM usuarios WHERE usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);

        if (!$stmt) {
            die("Error en la preparación de la consulta: " . $this->conexion->conexion->error);
        }

        $stmt->bind_param("s", $nombre);
        if (!$stmt->execute()) {
            die("Error al ejecutar la consulta: " . $stmt->error);
        }

        $resultado = $stmt->get_result();

        if ($resultado->num_rows > 0) {
            return $resultado->fetch_assoc();
        } else {
            error_log("Usuario no encontrado: " . $nombre); // Guardar en logs
            return null; // Usuario no existe
        }
    }


    public function actualizarUsuario($id_Usuario, $usuario, $contraseña, $rol)
    {
        $query = "UPDATE Usuarios SET usuario = ? , passw = ?, rol= ? WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssi", $usuario, $contraseña, $rol, $id_Usuario);

        if ($stmt->execute()) {
            echo "Usuario actualizado con éxito.";
        } else {
            echo "Error al actualizar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }

    public function eliminarUsuario($id_Usuario)
    {
        $query = "DELETE FROM usuarios WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_Usuario);

        if ($stmt->execute()) {
            echo "Usuario eliminado con éxito.";
        } else {
            echo "Error al eliminar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }
}
