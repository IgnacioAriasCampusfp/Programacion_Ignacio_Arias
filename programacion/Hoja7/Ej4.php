<?php
class Producto{

    public $nombre;
    public $precio;
    public function mostrarDetalles(){
        echo $this->nombre . " Precio: " . $this->precio;

    }
}
class Electrodomestico extends Producto{
    public $consumo;
    public function mostrarDetalles(){
        echo $this->nombre . " Precio: " . $this->precio . " Consumo: " . $this->consumo;

    }

}
$Product = new Producto;
$Product->nombre = "Macarrones";
$Product->precio = 3;
$Product->mostrarDetalles();

$Elect = new Electrodomestico;
$Elect->nombre = "Microondas";
$Elect->precio = 150;
$Elect-> consumo= "30W";
$Elect->mostrarDetalles();

?>