<?php


try{
    $contenido = file_get_contents("asd.txt");

    if ($contenido !== false) {
        $letras = strlen($contenido);
        echo $letras;
    } else {
        echo "Error al leer el archivo.";
    }
    
}
catch (Exception $e){
    echo "Error: " . $e->getMessage();
}
?>