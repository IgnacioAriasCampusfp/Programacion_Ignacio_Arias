<?php
require_once '../modelo/class_eventos.php';

class EventosController {
    private $modelo;

    public function __construct() {
        $this->modelo = new Eventos();
    }

    public function agregarEventos($evento, $fecha, $lugar) {
        $this->modelo->agregarEvento($evento, $fecha, $lugar);
    }

    public function listarEventos() {
        return $this->modelo->obtenerEventos();
    }

    public function obtenerEventosPorId($id_eventos) {
        return $this->modelo->obtenerEventosPorId($id_eventos);
    }

    public function actualizarEventos($id_eventos, $evento, $fecha, $lugar) {
        $this->modelo->actualizarEventos($id_eventos, $evento, $fecha, $lugar);
    }

    public function eliminarEventos($id_eventos) {
        $this->modelo->eliminarEventos($id_eventos);
    }
}
?>
