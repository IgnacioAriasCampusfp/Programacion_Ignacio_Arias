
public class Estudiante extends Persona {

	String curso;
	
	
	public Estudiante(String nombre, int edad, String curso) {
		super(nombre,edad);
		this.curso = curso;
		System.out.println("Estuiante registrado");
	}

	 @Override
	 public void mostrarDatos() {
		 super.mostrarDatos();
		 System.out.println("Curso: " + curso);
	 }	
}
