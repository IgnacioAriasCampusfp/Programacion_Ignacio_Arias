<?php


$eleccion = readline("Que quieres hacer: \n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n");


if ($eleccion == 1){
        $n1 = readline("Dime tu primer numero: ");
        $n2 = readline("Dime tu segundo numero: ");
        echo "Las suma de " . $n1 . " y " . $n2 . " es: " . $n1+$n2 . "\n";
}
elseif($eleccion == 2){
        $n1 = readline("Dime tu primer numero: ");
        $n2 = readline("Dime tu segundo numero: ");
        echo "Las resta de " . $n1 . " y " . $n2 . " es: " . $n1-$n2 . "\n";
}
elseif($eleccion == 3){
        $n1 = readline("Dime tu primer numero: ");
        $n2 = readline("Dime tu segundo numero: ");
        echo "Las resta de " . $n1 . " y " . $n2 . " es: " . $n1*$n2 . "\n";
}
elseif($eleccion == 4){
        $n1 = readline("Dime tu primer numero: ");
        $n2 = readline("Dime tu segundo numero: ");
        echo "Las resta de " . $n1 . " y " . $n2 . " es: " . $n1%$n2 . "\n";
}    
else{
        echo "No es opcion valida \n";
}

?>