<?php

$array = [];



for ($i=0; $i <= 10 ; $i++) { 
    $array[] = rand(1,100);
}

$t = count($array);

for ($i=0; $i < $t - 1; $i++) { 
    for ($j=0; $j < $t -1- $i; $j++) { 
        if ($array[$j] > $array[$j+1]) {
            $temp = $array[$j];
            $array[$j] = $array[$j+1];
            $array[$j + 1] = $temp;
        }

    }    
}

echo "Numeros ordenados: " . implode(" , " , $array) . "\n";
print_r($array)
?>