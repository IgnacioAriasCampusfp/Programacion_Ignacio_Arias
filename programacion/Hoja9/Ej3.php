<?php
class Usuario{
    protected $nombre;
    protected $email;

    public function __construct($nombre, $email)
    {
        $this->nombre = $nombre;
        $this->email = $email;
    }
    public function mostrarInfo(){
        return "Usuario: " . $this->nombre . " Email: " . $this->email . "\n";
    }

}
class Administrador extends Usuario{
    private $NivelAcceso;
    public function __construct($nombre, $email, $NivelAcceso)
    {
        parent::__construct($nombre, $email);
        $this->NivelAcceso = $NivelAcceso;
    }
    public function mostrarInfo(){
        return "Usuario: " . $this->nombre . " Email: " . $this->email . " Con nivel de acceso: ". $this->NivelAcceso ."\n" ;
    }

}
$nUser = new Usuario("Juana", "Juana@gmail.com");
echo $nUser->mostrarInfo();

$nAdmin = new Administrador("Pedro", "Pedrito@hotmail.com",4);
echo $nAdmin->mostrarInfo();

?>