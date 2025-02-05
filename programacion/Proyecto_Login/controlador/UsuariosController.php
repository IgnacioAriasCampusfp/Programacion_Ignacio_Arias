<?php
require_once '../modelo/class_usuarios.php';

class UsuariosController
{
    private $modelo;

    public function __construct()
    {
        $this->modelo = new Usuario();
    }

    public function agregarUsuario($usuario, $contraseña, $rol)
    {
        $this->modelo->agregarUsuario($usuario, $contraseña, $rol);
    }

    public function listarUsuarios()
    {
        return $this->modelo->obtenerUsuarios();
    }



    public function actualizarUsuario($id_usuario, $usuario, $contraseña, $rol)
    {
        $this->modelo->actualizarUsuario($id_usuario, $usuario, $contraseña, $rol);
    }

    public function eliminarUsuario($id_usuario)
    {
        $this->modelo->eliminarUsuario($id_usuario);
    }

    public function obtenerUsuarioPorNombre($usuario)
    {
        return $this->modelo->obtenerUsuarioPorNombre($usuario);
    }
}
