<?php

class Vehiculo{
	public $marca;
	public function encender(){
	return "Se encendió el coche";
}
}
class Coche extends Vehiculo{
	public $modelo;
}
$miCoche = new Coche;
$miCoche->marca="Aston Martin";
$miCoche->modelo = "Valkirye";
echo $miCoche->encender() . " de la marca y modelo " . $miCoche->marca . " " . $miCoche->modelo;

?>