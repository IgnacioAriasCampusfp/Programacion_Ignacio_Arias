package Hito;

public abstract class Animal {

	//Datos de los animales
	int num_chip;
	String nombre;
	int edad;
	String raza;
	boolean adoptado;
	
	//Constructor de la clase Animal
	public Animal(int num_chip, String nombre,int edad,String raza,boolean adoptado) {
		this.num_chip = num_chip;
		this.nombre = nombre;
		this.edad = edad;
		this.raza = raza;
		this.adoptado = adoptado;
		
	}
	//Metodo abstracto mostrar
	abstract void mostrar();
	
	
}
