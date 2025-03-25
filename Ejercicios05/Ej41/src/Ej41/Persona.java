package Ej41;

public class Persona {
	private String nombre;
	private int edad;
	public static void main(String[] args) {
		Persona persona1 = new Persona("Juna", 32);
		persona1.mostrarDatos();
		
	}
	public Persona(String nombre,int edad){
		this.edad = edad;
		this.nombre = nombre;
		
	}
	public void mostrarDatos() {
		System.out.println("Nombre: " + getNombre() + ", Edad: " + getEdad());
	}
	
	public String getNombre() {
		return nombre;
	}
	public int getEdad() {
		return edad;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
}
