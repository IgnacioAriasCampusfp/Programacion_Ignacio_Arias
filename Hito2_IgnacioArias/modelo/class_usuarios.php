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

}
