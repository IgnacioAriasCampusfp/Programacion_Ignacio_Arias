<?php
class RecetaAI {
    private string $url;
    private int $maxTokens;
    private float $temperature;

    public function __construct(string $host = 'http://localhost', int $puerto = 8000, int $maxTokens = 2100, float $temperature = 1) {
        $this->url = "$host:$puerto/v1/completions";
        $this->maxTokens = $maxTokens;
        $this->temperature = $temperature;
    }

    public function obtenerReceta(string $mensaje): string {
        if (empty($mensaje)) {
            return '';
        }

        $datos = [
            'prompt' => "$mensaje. Debe contener instrucciones, cantidades de ingredientes, tiempo de preparación y para cuántas personas. Máximo 2000 caracteres. Solo deben ser recetas en castellano.",
            'max_tokens' => $this->maxTokens,
            'temperature' => $this->temperature
        ];

        $jsonDatos = json_encode($datos);
        $ch = curl_init($this->url);

        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonDatos);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Content-Length: ' . strlen($jsonDatos)
        ]);

        $respuesta = curl_exec($ch);
        curl_close($ch);

        $respuestaDecodificada = json_decode($respuesta, true);
        return $respuestaDecodificada['choices'][0]['text'] ?? '';
    }
}
