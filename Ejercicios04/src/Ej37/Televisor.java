package Ej37;

public class Televisor extends Electrodomestico {
	int pulgadas ;
	public void mostrarDatos() {
		System.out.println("Marca: "+ marca + ", Precio: " + precio + ", Pulgadas: " + pulgadas);
		
	}
	public Televisor(String marca, double precio, int pulgadas) {
		this.marca = marca;
		this.precio = precio;
		this.pulgadas = pulgadas;
		
	}

}
