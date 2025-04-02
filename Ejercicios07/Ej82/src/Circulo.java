
public class Circulo extends Figura implements Calculable {

	double radio;
	final double PI = 3.14;
	public Circulo(double radio) {
		this.radio = radio;
		
	}
	public double calcularArea() {
		return radio * Math.pow(PI,2);
	}

}
