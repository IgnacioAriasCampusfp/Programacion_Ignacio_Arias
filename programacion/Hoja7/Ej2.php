<?php
class Rectangulo{

    public $base;
    public $altura;
    public function calcularArea(){

        return $this->base * $this->altura;

    }
}

$Rect = new Rectangulo;
$Rect->base = 2;
$Rect->altura = 4;
echo $Rect->calcularArea();


?>