
public class Electronico extends Item implements Describible {

	
	String marca;
	public Electronico(String marca) {
		this.marca = marca;
	}
	
	public String describir() {
		return "Electrodomestico de marca: " + marca;
	}

}
