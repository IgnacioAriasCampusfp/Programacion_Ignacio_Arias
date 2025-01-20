<?php
class Producto{
    private $nombre;
    private $precio;
    private $cantidad;

    public function __construct($nombre,$precio,$cantidad){
        $this->nombre = $nombre;
        $this->precio = $precio;
        $this->cantidad = $cantidad;
        

    }
    public function getNombre(){
        
        return $this->nombre;
        
    }
    public function getPrecio(){
       return $this->precio;
    }
    public function getCantidad(){
        return $this->cantidad;
    }
}

class ProductoImportado extends Producto{
    private $ImpuestoAdicional;
    function __construct($nombre,$precio,$cantidad,$ImpuestoAdicional){
        parent::__construct($nombre,$cantidad,$precio);
        $this->ImpuestoAdicional = $ImpuestoAdicional;

    }
    public function calcularPrecioFinal(){
        
        return $this->getCantidad() * $this->getPrecio() * $this->ImpuestoAdicional;
    }
}

$P = new Producto("Juan",23,2);
echo $P->getNombre() ." ". $P->getPrecio() ." ". $P->getCantidad(). "\n";

$PI = new ProductoImportado("Macarrones",2,23,1.21);
echo $PI->calcularPrecioFinal();
?>
