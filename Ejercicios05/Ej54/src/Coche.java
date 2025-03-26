
public class Coche extends Vehiculo{

	int numpuertas;
	
	public Coche(String marca, String modelo, int numpuertas) {
		super(marca, modelo);
		this.numpuertas = numpuertas;
	}
	
	@Override
	public void mostrarDatos() {
		super.mostrarDatos();
		System.out.println(numpuertas);
	}
}
