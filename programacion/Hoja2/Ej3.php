<?php



while (true) {
    $contraseña = readline("Introduce una contraseña de 8 caracteres con al menos 1 mayuscula, 1 minuscula y un numero: ");
    if (strlen($contraseña) < 8 || !preg_match("/[A-Z]/",$contraseña) || !preg_match("/[a-z]/",$contraseña) || !preg_match("/\d/", $contraseña)) {
        echo "Error al ingresar la contraseña \n";
    }
    else {
        echo "Contraseña aceptada";
        break;
    }
}

?>