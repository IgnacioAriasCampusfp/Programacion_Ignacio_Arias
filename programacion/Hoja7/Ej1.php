<?php

class Persona{
    public $nombre;
    public $edad;
    public $genero;

    public function presentar(){
        echo $this->nombre . " de edad: " . $this->edad . " y de genero: " . $this->genero;

    }
}

$miPersona = new Persona;
$miPersona->nombre = "Makoto";
$miPersona->edad = 16;
$miPersona->genero = "Puerta";

$miPersona->presentar();



?>