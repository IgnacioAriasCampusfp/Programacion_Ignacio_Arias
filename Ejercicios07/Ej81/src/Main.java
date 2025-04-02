import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {

		ArrayList<Animal> animales = new ArrayList<>();
		animales.add(new Perro("Firulais"));
		animales.add(new Gato("Wiskas"));
		animales.add(new Gato("Megatron"));
		animales.add(new Perro("Atom"));
		
		for(Animal animal : animales) {
			System.out.println(animal.nombre + " hace " + animal.hacerSonido());
		}
		
	}

}
