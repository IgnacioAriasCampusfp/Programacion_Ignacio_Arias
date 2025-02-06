<?php
class Conexion {
    
    private $servidor = 'localhost';
    private $usuario = 'root';
    private $password = 'curso';
    private $base_datos = 'HitoTareas2T';
    public $conexion;
    
    public function __construct() {
        //Conexión a la base de datos con mysqli 
        $this->conexion = new mysqli($this->servidor, $this->usuario, $this->password, $this->base_datos);
        //Si la conexión falla, se muestra un mensaje de error
        if ($this->conexion->connect_error) {
            die("Error de conexión: " . $this->conexion->connect_error);
        }
    }
    

    public function cerrar() {
        $this->conexion->close();
    }
}
?>
