<?php
$nombre = ["Alejandro","Sofía","Mateo","Valeria","Daniel","Camila","Lucas","Martina","Santiago","Isabella"];
$apellidos = ["García","Rodríguez","Martínez","Hernández","López","Pérez","Sánchez","Ramírez","Torres","Gómez"];

$nrandom = rand(1,10);
$arandom = rand(1,10);

echo "El nombre completo es: " . $nombre[$nrandom- 1] . " " . $apellidos[$arandom- 1];


?>