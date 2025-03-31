import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {

		ArrayList<Movible> movible = new ArrayList<>();
		Coche coche1 = new Coche("1");
		Coche coche2 = new Coche("2");
		Coche coche3 = new Coche("3");
		Bicicleta bici1 = new Bicicleta("1");
		Bicicleta bici2 = new Bicicleta("2");
		Bicicleta bici3 = new Bicicleta("3");


		movible.add(coche1);
		movible.add(coche2);
		movible.add(coche3);
		movible.add(bici1);
		movible.add(bici2);
		movible.add(bici3);

		for(Movible move : movible) {
			
			move.mover();
		}

		
	}

}
