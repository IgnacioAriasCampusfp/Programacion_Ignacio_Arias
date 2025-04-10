
public class Autobus extends Vehiculo {

	boolean movilidad_reducida;

	public Autobus(String codigo, int anio, int plazas, boolean movilidad) {
		super(codigo, anio, plazas);
		this.movilidad_reducida = movilidad;
	}

	@Override
	void mostrar() {
		System.out.println("Codigo del Vehiculo: " + codigo + ", Año de adquisición: " + anio + ", Numero de plazas: " + anio + ", Adaptado para movilidad: " + movilidad_reducida);
		
	}

		
}
