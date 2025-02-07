<?php
require_once '../modelo/class_usuarios.php';

class UsuariosController
{
    private $modelo;

    public function __construct()
    {
        $this->modelo = new Usuario();
    }

    public function agregarUsuario($usuario, $contraseña,$email, $rol)
    {
        $this->modelo->agregarUsuario($usuario, $contraseña,$email, $rol);
    }



    public function obtenerUsuarioPorEmail($email)
    {
        return $this->modelo->obtenerUsuarioPorEmail($email);
    }
}
