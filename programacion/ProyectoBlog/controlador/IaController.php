<?php
require_once '../modelo/class_ia.php';

class RecetaAIController {
    private $recetaAI;

    public function __construct() {
        $this->recetaAI = new RecetaAI();
    }

    public function generarReceta($mensaje) {
        if (empty($mensaje)) {
            return "Debes proporcionar una solicitud válida para la receta.";
        }

        return $this->recetaAI->obtenerReceta($mensaje);
    }
}
?>
