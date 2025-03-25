package Ej37;

public class Lavadora extends Electrodomestico {

	int capacidadKg;
	public void mostrarDatos() {
		System.out.println("Marca: "+ marca + ", Precio: " + precio + ", Capacidad: " + capacidadKg);	
	}
	public Lavadora(String marca, double precio, int capacidadKg) {
		this.marca = marca;
		this.precio = precio;
		this.capacidadKg = capacidadKg;
	}
}
