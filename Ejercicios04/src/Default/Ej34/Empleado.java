package Default.Ej34;

public class Empleado {

	public String nombre;
	private double saldo;
	protected String departamento;
	
	public void mostrarDatos() {
		System.out.println("Nombre: " + nombre + ", Saldo: " + saldo + ", Departamento: " + departamento);
		
	}
	public Empleado(String nombre, double saldo, String departamento){
		this.nombre = nombre;
		this.saldo = saldo;
		this.departamento = departamento;
	}
	

}
