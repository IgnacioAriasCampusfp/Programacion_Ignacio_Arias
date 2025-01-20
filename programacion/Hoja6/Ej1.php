<?php

Class Libro{
	public $titulo;
	public $autor;
	public $paginas;
	public function mostrarInfo(){
	return "Titulo: " . $this->titulo . " Autor: " . $this->autor . " Páginas: " . $this->paginas;
}
}
$miLibro = new Libro();
$miLibro->titulo = "El camino de los reyes";
$miLibro->autor = "Brandon Sanderson";
$miLibro->paginas = "1200";
echo $miLibro->mostrarInfo();
?>