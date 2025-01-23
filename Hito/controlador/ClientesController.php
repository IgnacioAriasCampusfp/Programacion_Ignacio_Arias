<?php
require_once '../modelo/class_cliente.php';

class ClientesController {
    private $modelo;

    public function __construct() {
        $this->modelo = new Cliente();
    }

    public function agregarCliente($nombre, $apellido, $email, $telefono, $fecha_nacimiento) {
        $this->modelo->agregarCliente($nombre, $apellido, $email, $telefono, $fecha_nacimiento);
    }

    public function listarClientes() {
        return $this->modelo->obtenerClientes();
    }

    public function obtenerClientePorId($id_Cliente) {
        return $this->modelo->obtenerClientePorId($id_Cliente);
    }

    public function actualizarCliente($id_Cliente, $nombre, $apellido, $email, $telefono, $fecha_nacimiento) {
        $this->modelo->actualizarCliente($id_Cliente, $nombre, $apellido, $email, $telefono, $fecha_nacimiento);
    }

    public function eliminarCliente($id_Cliente) {
        $this->modelo->eliminarCliente($id_Cliente);
    }
}
?>
