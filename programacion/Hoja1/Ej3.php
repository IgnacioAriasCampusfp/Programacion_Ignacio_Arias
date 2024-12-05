<?php

$n1 = readline("Dime el numero que quires saber si es primo: ");

for ($i=2; $i < $n1 ; $i++) { 
if ($n1%$i==0) {
    echo "No es primo";
    break;
}
else{
    echo "Es primo";
    break;
}

}


?>