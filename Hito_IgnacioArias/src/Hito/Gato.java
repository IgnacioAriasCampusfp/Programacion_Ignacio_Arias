package Hito;

public class Gato extends Animal {

	//Valores exclusivos de Gato
	boolean test_leucemia;
	
	//Constructor de Gato haciendo referencia al constructor del padre
	public Gato(int num_chip, String nombre, int edad, String raza, boolean adoptado, boolean test_leucemia) {
		super(num_chip, nombre, edad, raza, adoptado);
		this.test_leucemia = test_leucemia;
	}

	//Metodo mostrar que lo traemos de Animal y lo sobrescribimos
	@Override
	void mostrar() {
		System.out.println("Gato con Nº de chip: " + num_chip + " de nombre: " + nombre + " Edad: " + edad + ", raza: " + raza + ", Adoptado: " + adoptado + ", con test de leucemia: "  + test_leucemia);
		
	}

}
