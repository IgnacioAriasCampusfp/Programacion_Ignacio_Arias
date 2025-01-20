<?php

class Empleado{
    public $nombre;
    public $sueldo;
    public function mostrarDetalles(){
        echo $this->nombre . $this->sueldo;
        }
    }
class Gerente extends Empleado{
        public $departamento;
        public function mostrarDetalles(){
            echo $this->nombre . $this->sueldo . $this->departamento;
            }
}
$miEmpleado = new Empleado;
$miEmpleado->nombre = "Juan ";
$miEmpleado->sueldo = " 3 eurillos ";
$miEmpleado->mostrarDetalles();

$miGerente = new Gerente;
$miGerente->nombre = "Pedro ";
$miGerente->sueldo = "15000 pesetas ";
$miGerente->departamento = "Bricolaje ";
$miGerente->mostrarDetalles();



?>