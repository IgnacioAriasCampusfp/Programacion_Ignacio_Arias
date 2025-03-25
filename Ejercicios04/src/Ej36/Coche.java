package Ej36;

public class Coche extends Vehiculo{

	public Coche(String marca, String modelo) {
		this.modelo  = modelo;
		this.marca = marca;
	}
	public void mostrarDatos() {
		System.out.println("Marca = " + marca + " ,Modelo: "+ modelo);
		
	}
	public void describir() {
		System.out.println("Soy un coche de marca " + marca + " y modelo " + modelo);
		
	}

}
