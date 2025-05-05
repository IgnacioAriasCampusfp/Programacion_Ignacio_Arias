import java.io.Serializable;

public class Animal implements Serializable {
	String nombre;
	String especie;
	
	
	public Animal(String nombre,String especie) {
		this.nombre = nombre;
		this.especie = especie;
	}
}
