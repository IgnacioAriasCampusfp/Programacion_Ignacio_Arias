<?php

class Carrito {
    public $productos = [];

    public function agregarProducto($nombre, $precio, $cantidad) {
        $this->productos[] = [
            'nombre' => $nombre,
            'precio' => $precio,
            'cantidad' => $cantidad
        ];
    }

    public function quitarProducto($nombre) {
        foreach ($this->productos as $indice => $producto) {
            if ($producto['nombre'] === $nombre) {
                unset($this->productos[$indice]);
                $this->productos = array_values($this->productos); 
                return;
            }
        }
        echo "Producto no encontrado: $nombre\n";
    }

    public function calcularTotal() {
        $total = 0;
        foreach ($this->productos as $producto) {
            $total += $producto['precio'] * $producto['cantidad'];
        }
        return $total;
    }

    public function mostrarDetalleCarrito() {
        if (empty($this->productos)) {
            echo "El carrito está vacío.\n";
            return;
        }

        echo "Detalles del carrito:\n";
        foreach ($this->productos as $producto) {
            echo "Producto: {$producto['nombre']}, Precio: {$producto['precio']}, Cantidad: {$producto['cantidad']}\n";
        }
        echo "Total: {$this->calcularTotal()}\n";
    }
}

// Simulación de uso del carrito
$carrito = new Carrito();
$carrito->agregarProducto("Manzanas", 1.2, 5);
$carrito->agregarProducto("Pan", 2.5, 2);
$carrito->agregarProducto("Leche", 1.5, 3);

// Mostrar detalles del carrito
$carrito->mostrarDetalleCarrito();

// Quitar un producto
$carrito->quitarProducto("Pan");

// Mostrar detalles después de quitar un producto
$carrito->mostrarDetalleCarrito();

?>
