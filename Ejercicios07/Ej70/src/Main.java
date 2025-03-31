import java.util.Arrays;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] numeros = new int[5];
		System.out.println("Introduce 5 numeros");
		for(int i = 0; i < numeros.length; i++) {
			numeros[i] = scanner.nextInt();
		}
		System.out.println("Numeros ingresados: " + Arrays.toString(numeros));
	}

}
