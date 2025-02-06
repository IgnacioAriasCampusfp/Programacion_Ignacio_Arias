<?php
require_once '../modelo/class_tarea.php';

class TareasController {
    private $modelo;

    public function __construct() {
        $this->modelo = new Tarea();
    }

    public function agregarTarea($email, $titulo, $descripcion, $estado) {
        $this->modelo->agregarTarea($email, $titulo, $descripcion, $estado);
    }

    public function listarTareas($email) {
        return $this->modelo->obtenerTareasPorEmail($email);
    }


    public function actualizarTarea($id_Tarea, $estado) {
        $this->modelo->actualizarTarea($id_Tarea, $estado);
    }

    public function eliminarTarea($id_Tarea) {
        $this->modelo->eliminarTarea($id_Tarea);
    }
}
?>
