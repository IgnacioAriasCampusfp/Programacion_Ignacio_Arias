<?php
class Circulo{
	public $radio;
public function calcularArea(){
	echo "El area del circulo es: " . 3.14 * $this->radio**2;
}

}
$miCirculo = new Circulo();
$miCirculo->radio = 5;
$miCirculo->calcularArea();



?>