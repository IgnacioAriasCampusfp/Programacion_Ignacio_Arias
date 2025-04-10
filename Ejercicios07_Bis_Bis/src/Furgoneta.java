
public class Furgoneta extends Vehiculo {
	String tipo_carga;
	
	public Furgoneta(String codigo, int anio, int plazas, String tipo) {
		super(codigo, anio, plazas);
		this.tipo_carga = tipo;
	}
	@Override
	void mostrar() {
		System.out.println("Codigo del Vehiculo: " + codigo + ", Año de adquisición: " + anio + ", Numero de plazas: " + anio + ", Tipo de carga: " + tipo_carga);
		
	}

}
