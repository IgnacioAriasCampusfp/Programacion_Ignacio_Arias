
public class Rectangulo extends Figura implements Calculable {

	double ancho;
	double alto;
	public Rectangulo(double ancho, double alto) {
		this.alto = alto;
		this.ancho = ancho;
		
	}
	
	public double calcularArea() {
		return alto * ancho;
	}

}
