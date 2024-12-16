<?php


$archivo = fopen("datos.txt", "w"); // Modo escritura

if ($archivo) {
   
    fclose($archivo);
} else {
    echo "Error al abrir el archivo.";
}

/*
$archivo = fopen("datos.txt", "r");

if ($archivo) {
    echo "Archivo abierto con éxito. -------- \n";
    $contenido = fread($archivo, filesize("datos.txt")); // Leer todo el archivo
    echo $contenido;

    fclose($archivo); // Cerrar el archivo
} else {
    echo "Error al abrir el archivo.";
}
*/
/*
if (unlink("datos.txt")) {
    echo "Archivo eliminado con éxito.";
} else {
    echo "Error al eliminar el archivo.";
}
*/

function Menu(){
try{
    $opciones = readline("Menu: \n1. Crear archivo de texto\n2. Escribir texto\n3. Leer texto\n4. Añadir más texto \n");
    switch($opciones){
        case 1:
            Create();
            break;
        case 2:
            Write();
            break;
        case 3:
            Read();
            break;
        case 4:
            WritePlus();
            break;
    }
}
catch (Exception $e){
    echo "Error: " . $e->getMessage();
}

}
function Create(){
    try{
        $nombrearchivo = readline("Dime el nombre del archivo sin escribir .txt: ");
        $narchivo = $nombrearchivo . ".txt";

        $archivo = fopen($narchivo, "w"); // Modo escritura

        if ($archivo) {
           
            fclose($archivo);
        } else {
            echo "Error al crear el archivo.\n";
        }
    }
    catch(Exception $e){
        echo "Error: ". $e->getMessage();
    }
}
function Write(){
    try{
        $nombrearchivo = readline("Dime el nombre del archivo que deseas escribir, sin escribir .txt: ");
        $narchivo = $nombrearchivo . ".txt";

        $archivo = fopen($narchivo, "w"); // Modo escritura

        if ($archivo) {
            while (true) {
                $texto = readline("Texto que deseas introducir: ");
                if ($texto == "No") {
                    break;
                }else{

                    $fecha = new DateTime();
                    $stringDate = $fecha->format('Y-m-d H:i:s') . "\n";
                    fwrite($archivo,$stringDate);
                   
                    $textof = $texto . "\n";
                    fwrite($archivo, $textof);
                }
                
                
                
            }
            fclose($archivo);
        } else {
            echo "Error al crear el archivo.\n";
        }
    }
    catch(Exception $e){
        echo "Error: ". $e->getMessage();
    }
}
function Read(){
    $nombrearchivo = readline("Dime el nombre del archivo que deseas escribir, sin escribir .txt: ");
    $narchivo = $nombrearchivo . ".txt";
    echo "Contenido actualizado del archivo:\n";
    echo file_get_contents($narchivo);

}
function WritePlus(){
    $nombrearchivo = readline("Dime el nombre del archivo que deseas escribir, sin escribir .txt: ");
    $narchivo = $nombrearchivo . ".txt";
    $fecha = new DateTime();
    $stringDate = $fecha->format('Y-m-d H:i:s') . "\n";
    $Texto = readline("Que quieres añadir al archivo: ");
    $textoF = $stringDate .  $Texto . "\n";
    //write($archivo,$stringDate);
    file_put_contents($narchivo, $textoF, FILE_APPEND);
    echo "Texto añadido con éxito.\n";

}
Menu();


?>