
public class Main {

	public static void main(String[] args) {
		
		Estudiante estudiante = (Estudiante) new Persona("Alberto",13);
		Profesor profe = (Profesor) new Persona("Don Ignacio",54);
		System.out.println(profe instanceof Profesor);
		System.out.println(estudiante instanceof Estudiante);


		
		
		
		//Persona profe = new Profesor("Don Ignacio",54,"Lengua");
		//Persona estudiante = new Estudiante("Alberto",13,"2º ESO");
		//estudiante.mostrarDatos();
		//profe.mostrarDatos();
		
		
		
	}

}
