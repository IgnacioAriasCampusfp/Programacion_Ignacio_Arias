public class Calculadora{
public static void main(String[] args){
Calculadora calc = new Calculadora();
System.out.println(calc.doble(5));

}

public double doble(int numero){
double numdoble = (double) numero;
return numdoble;
}
}