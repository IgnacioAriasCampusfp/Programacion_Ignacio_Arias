
public class EmpleadoPorHoras extends Empleado implements Pagable {

	int horasTrabajadas;
	double tarifaHora;
	
	public EmpleadoPorHoras(int id, String nombre,int horasTrabajadas, double tarifaHora) {
		this.id = id;
		this.nombre = nombre;
		this.horasTrabajadas = horasTrabajadas;
		this.tarifaHora = tarifaHora;
		
	}
	
	public double calcularSalarioMensual() {
		return horasTrabajadas * tarifaHora;
	}

}
