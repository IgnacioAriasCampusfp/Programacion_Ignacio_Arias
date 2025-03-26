public class Circulo extends Figura {
	
    double radio;

    @Override
    double calcularArea() {
        return Math.PI * radio * radio;
    }
}
