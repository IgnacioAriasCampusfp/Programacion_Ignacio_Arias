
public class Main {

	public static void main(String[] args) {
		Cuadrado cuad = new Cuadrado();
		cuad.lado = 2;
		cuad.calcularArea();
		Triangulo tri = new Triangulo();
		tri.altura = 10;
		tri.base = 4;
		tri.calcularArea();
	}

}
