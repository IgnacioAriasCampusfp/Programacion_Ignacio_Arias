import java.io.*;
public class Empleado implements Serializable{
	String nombre;
	int edad;
	double salario;
	
	public Empleado(String nombre,int edad,double salario) {
		this.nombre = nombre;
		this.edad = edad;
		this.salario = salario;
	}
	
}
