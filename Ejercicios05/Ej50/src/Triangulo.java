
public class Triangulo extends Figura{
	int base;
	int altura;
	
	public Triangulo(int base,int altura){
		this.altura = altura;
		this.base = base;
		
	}
	
	@Override
    double calcularArea() {
        return (base * altura) / 2;
    }

}
