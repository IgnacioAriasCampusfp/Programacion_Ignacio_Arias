<?php 


$random = rand(1,100);


while (true){
    $n1 = readline("Dime el numero para intentar adivinar: ");
    if ($n1 == $random) {
        echo "Ganaste";
        break;
    }
}
?>