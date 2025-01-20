<?php

class CuentaBancaria{
    private $titular;
    private $tipoDeCuenta;
    private $saldo;
    public function __construct($titular,$tipoDeCuenta)
    {
        $this->titular = $titular;
        $this->tipoDeCuenta = $tipoDeCuenta;
        $saldo = 0;
        $this->saldo = $saldo;
        
    }
    public function detalles(){
        return "Titular: " . $this->titular . " Tipo de Cuenta: " . $this->tipoDeCuenta . " Saldo: " . $this->saldo . "\n";
    }
    public function depositar($cantidad){
        $this->saldo += $cantidad;
    }
    public function retirar($cantidad){
       if($this->verificarSaldoSuficiente($cantidad)){
        echo "No tienes dinero suficiente \n";
       }
       else{
        $this->saldo -= $cantidad;
       }
    }
    private function verificarSaldoSuficiente($cantidad){
        
           return $cantidad > $this->saldo;
        
    }



}
$User = new CuentaBancaria("Juan", "Plus");
$User->depositar(240);
$User->retirar(230);
$User->depositar(1340);
echo $User->detalles();
$User->retirar(3000);


?>