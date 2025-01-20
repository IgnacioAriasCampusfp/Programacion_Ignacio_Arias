<?php
class Calculadora{

    public function sumar($n1, $n2){
        echo $n1 + $n2 . "\n";

    }
    public function restar($n1, $n2){
        echo $n1 - $n2. "\n";

    }
    public function mult($n1, $n2){
        echo $n1 * $n2. "\n";

    }
    public function div($n1, $n2){
        try{
        if ($n2 == 0){
            throw new Exception("No se puede dividir entre cero. ");
        }else{
            echo $n1 / $n2. "\n";
        }
    }

    catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
    }
    
    

}

$Calc = new Calculadora;

$Calc->sumar(4,5);
$Calc->restar(4,5);
$Calc->mult(4,5);
$Calc->div(4,2);

?>