<?php

class CuentaBancaria {
    public $titular;
    public $saldo;
    public $tipoDeCuenta;

    public function configurarCuenta($titular, $saldoInicial, $tipoDeCuenta) {
        $this->titular = $titular;
        $this->saldo = $saldoInicial;
        $this->tipoDeCuenta = $tipoDeCuenta;
    }

    public function depositar($cantidad) {
        if ($cantidad > 0) {
            $this->saldo += $cantidad;
            echo "Depósito exitoso. Nuevo saldo: {$this->saldo}\n";
        } else {
            echo "La cantidad a depositar debe ser positiva.\n";
        }
    }

    public function retirar($cantidad) {
        if ($cantidad <= $this->saldo && $cantidad > 0) {
            $this->saldo -= $cantidad;
            echo "Retiro exitoso. Nuevo saldo: {$this->saldo}\n";
        } elseif ($cantidad > $this->saldo) {
            echo "Fondos insuficientes para realizar el retiro.\n";
        } else {
            echo "La cantidad a retirar debe ser positiva.\n";
        }
    }

    public function mostrarInfo() {
        echo "Titular: {$this->titular}\n";
        echo "Tipo de cuenta: {$this->tipoDeCuenta}\n";
        echo "Saldo actual: {$this->saldo}\n";
    }
}

// Crear una instancia de CuentaBancaria
$cuenta = new CuentaBancaria();
$cuenta->configurarCuenta("Juan Pérez", 5000, "Ahorro");

// Realizar operaciones
$cuenta->depositar(1500);
$cuenta->retirar(2000);
$cuenta->retirar(5000);
$cuenta->depositar(-300);
$cuenta->retirar(0);

// Mostrar información final
$cuenta->mostrarInfo();

?>
