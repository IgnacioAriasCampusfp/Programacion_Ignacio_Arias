
public class EmpleadoFijo extends Empleado implements Pagable {

	double salarioBase;
	public EmpleadoFijo(int id, String nombre, double salarioBase) {
		this.id = id;
		this.nombre = nombre;
		this.salarioBase = salarioBase;
		
	}
	public double calcularSalarioMensual() {
		return salarioBase;
	}

	
	
}
