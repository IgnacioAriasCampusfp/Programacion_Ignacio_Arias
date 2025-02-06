<?php
require_once '../config/class_conexion.php';

class Usuario
{
    private $conexion;

    public function __construct()
    {
        $this->conexion = new Conexion();
    }
    //Metodo para agregar un usuario atraves de los parametros usuario, passw, email y rol a la base de datos
    public function agregarUsuario($usuario, $passw, $email, $rol)
    {
        //Encriptamos la contraseña atraves de la funcion password_hash
        $hashedPassword = password_hash($passw, PASSWORD_DEFAULT);
        //Preparamos la consulta para agregar un usuario
        $query = "INSERT INTO usuarios (usuario, passw, email, rol) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssss", $usuario, $hashedPassword, $email, $rol);

        //Si la consulta se ejecuta correctamente, se muestra un mensaje de exito
        if ($stmt->execute()) {
            echo "Usuario agregado con éxito.";
        } else {
            echo "Error al agregar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }

    //Metodo para obtener todos los usuarios de la base de datos atraves del email
    public function obtenerUsuarioPorEmail($email)
    {
        $query = "SELECT * FROM usuarios WHERE email = ?";
        $stmt = $this->conexion->conexion->prepare($query);

        if (!$stmt) {
            die("Error en la preparación de la consulta: " . $this->conexion->conexion->error);
        }

        $stmt->bind_param("s", $email);
        //Si la consulta no se ejecuta correctamente, se muestra un mensaje de error
        if (!$stmt->execute()) {
            die("Error al ejecutar la consulta: " . $stmt->error);
        }

        $resultado = $stmt->get_result();
        //Si el resultado de la consulta es mayor a 0, se retorna el resultado
        if ($resultado->num_rows > 0) {
            return $resultado->fetch_assoc();
        }//Si no, se muestra un mensaje de error 
        else {
            error_log("Usuario no encontrado: " . $email); 
            return null; 
        }
    }

    //Funcion para actualizar un usuario atraves de los parametros
    public function actualizarUsuario($id_Usuario, $usuario, $passw, $rol)
    {
        //Consulta para actualizar un usuario
        $query = "UPDATE Usuarios SET usuario = ? , passw = ?, rol= ? WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("sssi", $usuario, $passw, $rol, $id_Usuario);
        //Si la consulta se ejecuta correctamente, se muestra un mensaje de exito sino, se muestra un mensaje de error
        if ($stmt->execute()) {
            echo "Usuario actualizado con éxito.";
        } else {
            echo "Error al actualizar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }

    //Funcion para eliminar un usuario atraves del id del usuario
    public function eliminarUsuario($id_Usuario)
    {
        $query = "DELETE FROM usuarios WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_Usuario);
        //Si la consulta se ejecuta correctamente, se muestra un mensaje de exito sino, se muestra un mensaje de error
        if ($stmt->execute()) {
            echo "Usuario eliminado con éxito.";
        } else {
            echo "Error al eliminar Usuario: " . $stmt->error;
        }

        $stmt->close();
    }
}
