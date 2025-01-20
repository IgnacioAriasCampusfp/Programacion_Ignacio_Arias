<?php
class Conversor{


    public function DolarEuro($n1){
        return $n1 * 1.02 . "\n";

    }
    public function EuroDolar($n1){
        return $n1 * 0.98. "\n";

    }
}


$Convert = new Conversor;

echo $Convert->DolarEuro(4);
echo $Convert->EuroDolar(6);
?>