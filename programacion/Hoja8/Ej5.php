<?php

class Personaje {
    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;

    public function configurarPersonaje($nombre, $nivel, $puntosVida, $puntosAtaque) {
        $this->nombre = $nombre;
        $this->nivel = $nivel;
        $this->puntosVida = $puntosVida;
        $this->puntosAtaque = $puntosAtaque;
    }

    public function atacar(Personaje $objetivo) {
        $daño = $this->puntosAtaque;
        $objetivo->reducirVida($daño);
        echo "{$this->nombre} ataca a {$objetivo->getNombre()} causando {$daño} puntos de daño.\n";
    }

    public function reducirVida($cantidad) {
        $this->puntosVida -= $cantidad;
        if ($this->puntosVida < 0) {
            $this->puntosVida = 0;
        }
    }

    public function curarse() {
        $vidaRestaurada = 10 * $this->nivel;
        $this->puntosVida += $vidaRestaurada;
        echo "{$this->nombre} se cura y restaura {$vidaRestaurada} puntos de vida.\n";
    }

    public function subirNivel() {
        $this->nivel++;
        $this->puntosAtaque += 5;
        $this->puntosVida += 20;
        echo "{$this->nombre} sube al nivel {$this->nivel}. Mejora sus puntos de ataque y vida.\n";
    }

    public function getNombre() {
        return $this->nombre;
    }

    public function mostrarEstado() {
        echo "Nombre: {$this->nombre}, Nivel: {$this->nivel}, Vida: {$this->puntosVida}, Ataque: {$this->puntosAtaque}\n";
    }
}

// Crear personajes
$personaje1 = new Personaje();
$personaje1->configurarPersonaje("Guerrero", 1, 100, 15);

$personaje2 = new Personaje();
$personaje2->configurarPersonaje("Mago", 1, 80, 20);

// Mostrar estado inicial
$personaje1->mostrarEstado();
$personaje2->mostrarEstado();

// Simulación de batalla
$personaje1->atacar($personaje2);
$personaje2->mostrarEstado();

$personaje2->curarse();
$personaje2->mostrarEstado();

$personaje1->subirNivel();
$personaje1->mostrarEstado();

?>
