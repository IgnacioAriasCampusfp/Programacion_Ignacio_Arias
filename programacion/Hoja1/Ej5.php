<?php

$altura = readline("Que altura quereis la altura: ");

for ($i=1; $i <= $altura ; $i++) { 
    for ($n=1; $n < $altura - $i; $n++) { 
        echo " ";

    }
    for ($n=1; $n <= $i ; $n++) { 
        echo $n;

    }
    echo " \n";
}
?> 