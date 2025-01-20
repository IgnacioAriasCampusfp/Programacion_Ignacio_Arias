<?php

class Empleado {
    public $nombre;
    public $sueldo;
    public $añosExperiencia;

    public function configurarEmpleado($nombre, $sueldo, $añosExperiencia) {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
        $this->añosExperiencia = $añosExperiencia;
    }

    public function calcularBonus() {
        return ($this->sueldo * 0.05) * floor($this->añosExperiencia / 2);
    }

    public function mostrarDetalles() {
        echo "Nombre: {$this->nombre}\n";
        echo "Sueldo: {$this->sueldo}\n";
        echo "Años de experiencia: {$this->añosExperiencia}\n";
        echo "Bono: {$this->calcularBonus()}\n";
    }
}

class Consultor extends Empleado {
    public $horasPorProyecto;

    public function configurarConsultor($nombre, $sueldo, $añosExperiencia, $horasPorProyecto) {
        parent::configurarEmpleado($nombre, $sueldo, $añosExperiencia);
        $this->horasPorProyecto = $horasPorProyecto;
    }

    public function calcularBonus() {
        $bonusBase = parent::calcularBonus();
        if ($this->horasPorProyecto > 100) {
            $bonusBase += 1000; // Bono adicional por horas
        }
        return $bonusBase;
    }

    public function mostrarDetalles() {
        parent::mostrarDetalles();
        echo "Horas por proyecto: {$this->horasPorProyecto}\n";
    }
}

// Crear instancias
$empleado = new Empleado();
$empleado->configurarEmpleado("Juan Pérez", 50000, 6);

$consultor = new Consultor();
$consultor->configurarConsultor("Ana López", 70000, 8, 120);

// Mostrar detalles y comparar bonificaciones
echo "Detalles del Empleado:\n";
$empleado->mostrarDetalles();

echo "\nDetalles del Consultor:\n";
$consultor->mostrarDetalles();

?>
