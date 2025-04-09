package Hito;

public class Perro extends Animal {
	//Valores exclusivos de Perro

	String size;
	
	//Constructor de Perro haciendo referencia al constructor del padre

	public Perro(int num_chip, String nombre, int edad, String raza, boolean adoptado, String size) {
		super(num_chip, nombre, edad, raza, adoptado);
		this.size = size;
	}

	//Metodo mostrar que lo traemos de Animal y lo sobrescribimos

	@Override
	void mostrar() {
		System.out.println("Perro con Nº de chip: " + num_chip + " de nombre: " + nombre + " Edad: " + edad + ", raza: " + raza + ", Adoptado: " + adoptado + ", con tamaño "  + size);
	}

	
}
