<?php
require_once '../modelo/class_cliente.php';

// Controlador para la gestión de clientes
class ClientesController {
    private $modelo;

    // Constructor de cliente
    public function __construct() {
        $this->modelo = new Cliente();
    }
    // Funcion para agregar un cliente
    public function agregarCliente($nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion) {
        $this->modelo->agregarCliente($nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion);
    }
    // Funcion para listar los clientes
    public function listarClientes() {
        return $this->modelo->obtenerClientes();
    }
    // Funcion para obtener un cliente por su ID
    public function obtenerClientePorId($id_Cliente) {
        return $this->modelo->obtenerClientePorId($id_Cliente);
    }
    // Funcion para actualizar un cliente
    public function actualizarCliente($id_Cliente, $nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion) {
        $this->modelo->actualizarCliente($id_Cliente,$nombre,$apellidos, $correo, $Edad,$PlanBase,$PaquetesAdicionales,$Duracion);
    }
    // Funcion para eliminar un cliente
    public function eliminarCliente($id_Cliente) {
        $this->modelo->eliminarCliente($id_Cliente);
    }

    

}
?>
