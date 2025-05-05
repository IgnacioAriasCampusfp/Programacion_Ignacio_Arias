import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Numero 1:");
		int n1 = scan.nextInt();
		System.out.println("Numero 2:");
		int n2 = scan.nextInt();
		try {
			System.out.println(n1 / n2);
		}catch(ArithmeticException e){
			System.out.println("No se puede dividir entre cero");
		}
		
	}

}
