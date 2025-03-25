public class Verificador{
public static void main(String[] args){
	Verificador veri = new Verificador();
	System.out.println(veri.esMayorYPar(14));
	System.out.println(veri.esMayorYPar(2));

}
public boolean esMayorYPar(int numero){
return numero>10 && numero%2==0;
}
}