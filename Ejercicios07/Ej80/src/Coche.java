
public class Coche extends Vehiculo implements Movible  {

	public Coche(String id) {
		super(id);
		
	}
	
	public void mover() {
		System.out.println("El coche " + id + " se mueve por el asfalto.");
	}

}
