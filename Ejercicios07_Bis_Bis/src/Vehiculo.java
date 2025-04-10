
public abstract class Vehiculo {
	String codigo;
	int anio;
	int plazas;

	public Vehiculo(String codigo, int anio, int plazas) {
		this.codigo = codigo;
		this.anio = anio;
		this.plazas = plazas;
		
	}
	abstract void mostrar();
}
