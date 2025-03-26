
public class Cuadrado extends Figura {
	
	int lado;
	public Cuadrado(int lado) {
		this.lado = lado;
		
	}
	
	@Override
    double calcularArea() {
        return lado * lado;
    }

}
