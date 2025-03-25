package Ej31;

public class Persona {
	String nombre;
	int edad;
	public static void main(String[] args) {
		Persona persona1 = new Persona();
		persona1.nombre = "Juan";
		persona1.edad = 22;
		persona1.mostrarDatos();
		Persona persona2 = new Persona();
		persona2.edad = 12;
		persona2.nombre = "Pablo";
		persona2.mostrarDatos();
	
		
	}
	public void mostrarDatos() {
		System.out.println(nombre);
		System.out.println(edad);

		
	}
}
