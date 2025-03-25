public class Conversor{
public static void main(String[] args){
	Conversor conversor = new Conversor();
	conversor.convertirDobleAInt(100.84);
}
public void convertirDobleAInt(double  numero){
int entero = (int) numero;
System.out.println(entero);
System.out.println(numero);

}
}