
public class Profesor extends Persona{
	String asignatura;
	
	public Profesor(String nombre, int edad, String asignatura) {
		super(nombre,edad);
		this.asignatura = asignatura;
		
	}
	@Override
	public void mostrarDatos() {
		System.out.println("Nombre: " + getNombre() + ", Edad: " + getEdad() + ", Asignatura: " + asignatura );

		
	}

}
