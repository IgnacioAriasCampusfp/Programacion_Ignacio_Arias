<?php

class Tarea {
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public $estado;

    public function configurarTarea($nombre, $descripcion, $fechaLimite) {
        $this->nombre = $nombre;
        $this->descripcion = $descripcion;
        $this->fechaLimite = $fechaLimite;
        $this->estado = "pendiente";
    }

    public function marcarComoCompletada() {
        $this->estado = "completada";
    }

    public function editarDescripcion($nuevaDescripcion) {
        $this->descripcion = $nuevaDescripcion;
    }

    public function mostrarTarea() {
        echo "Nombre: {$this->nombre}\n";
        echo "Descripción: {$this->descripcion}\n";
        echo "Fecha límite: {$this->fechaLimite}\n";
        echo "Estado: {$this->estado}\n";
    }
}

// Crear lista de tareas
$tareas = [];
$tarea1 = new Tarea();
$tarea1->configurarTarea("Comprar víveres", "Comprar frutas y verduras", "2025-01-20");
$tareas[] = $tarea1;

$tarea2 = new Tarea();
$tarea2->configurarTarea("Estudiar", "Repasar para el examen de matemáticas", "2025-01-18");
$tareas[] = $tarea2;

$tarea3 = new Tarea();
$tarea3->configurarTarea("Hacer ejercicio", "Completar 30 minutos de cardio", "2025-01-15");
$tareas[] = $tarea3;

// Marcar algunas tareas como completadas
$tareas[0]->marcarComoCompletada();

// Editar la descripción de una tarea
$tareas[1]->editarDescripcion("Repasar para el examen de física");

// Mostrar todas las tareas
foreach ($tareas as $tarea) {
    $tarea->mostrarTarea();
    echo "\n";
}

?>
