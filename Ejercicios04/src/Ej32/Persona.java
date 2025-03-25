package Ej32;

public class Persona {
	String nombre;
	int edad;
	public static void main(String[] args) {
		Persona persona1 = new Persona();
		persona1.mostrarDatos();
		Persona persona2 = new Persona("Pablo");
		persona2.mostrarDatos();
		Persona persona3 = new Persona("Juan" , 123);
		persona3.mostrarDatos();
	
		
	}
	public Persona() {
        this.nombre = "Desconocido";
        this.edad = 0;
    }
    
    public Persona(String nombre) {
        this.nombre = nombre;
        this.edad = 0;
    }
    
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

	public void mostrarDatos() {
		System.out.println(nombre + edad);

		
	}
}
