
public class Bicicleta extends Vehiculo implements Movible {

	public Bicicleta(String id) {
		super(id);
	}

	
	public void mover() {

		System.out.println("La bicileta " + id + " se mueve por el carril bici");
	}

}
