<?php

class Empleado{

    private $nombre;
    private $sueldo;
    private $puesto;

    public function __construct($nombre, $sueldo, $puesto)
    {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
        $this->puesto = $puesto;
    }
    public function setSueldo($nuevoSueldo){
        $this->sueldo = $nuevoSueldo;
    }
    public function getSueldo(){
        return $this->sueldo;
    }
    public function getNombre(){
        return $this->nombre;
    }
    public function getPuesto(){
        return $this->puesto;
    }
}
class Gerente extends Empleado{
    private $departamento;

    public function __construct($nombre, $sueldo, $puesto,$departamento)
    {
        parent::__construct($nombre, $sueldo, $puesto);
        $this->departamento = $departamento;
    }
    public function revisarEmpleado(Empleado $empleado){
       return "Nombre: " .  $empleado->getNombre(). " Puesto: " . $empleado->getPuesto();

    }

}
$E1 = new Empleado("Juan", 1500, "Sketch");
$E2 = new Empleado("Pedro", 1250, "Marketing");

$G1 = new Gerente("Francisco", 3000,"Gerente","RRSS");
echo $G1->revisarEmpleado($E1);
echo $G1->revisarEmpleado($E2);

?>