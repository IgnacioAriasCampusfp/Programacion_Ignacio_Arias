<?php

class Vehiculo {
    private $marca;
    private $modelo;
    public function __construct($marca,$modelo)
    {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }
    public function getMarca() {
        return $this->marca;
    }

    public function getModelo() {
        return $this->modelo;
    }
    public function enceder(){
        echo "Brum brum \n";
    }
}
class Coche extends Vehiculo{
    private $combustible;
    public function __construct($marca,$modelo,$combustible)
    {
        parent::__construct($marca,$modelo);
        $this->combustible = $combustible;
    }
    public function mostrarDetalles(){

        return "Marca: " . parent::getMarca() . " Modelo:" . $this->getModelo() . " Tipo de combustible: " . $this->combustible;
    }
}
$nVehiculo = new Vehiculo("Toyota","Corolla");
echo $nVehiculo->enceder();

$nCoche = new Coche("Toyota","Trueno","Gasolina");
$nCoche->enceder();
echo $nCoche->mostrarDetalles();

?>