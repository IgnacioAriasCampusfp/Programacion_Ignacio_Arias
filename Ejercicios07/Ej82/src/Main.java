import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		double total = 0;
		ArrayList<Figura> figuras = new ArrayList<>();
		figuras.add(new Circulo(3));
		figuras.add(new Circulo(8));
		figuras.add(new Circulo(33));
		figuras.add(new Rectangulo(3,32));
		figuras.add(new Rectangulo(12,3));
		figuras.add(new Rectangulo(98156,31884));

		for(Figura fig : figuras) {
			total += fig.calcularArea();
			
		}
		System.out.println(total);
	}

}
