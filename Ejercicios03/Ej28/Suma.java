import java.util.Scanner;

public class Suma {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;
        int suma = 0;

        do {
            System.out.print("Ingrese un número (0 para salir): ");
            numero = scanner.nextInt();
            suma += numero; 
            System.out.println("Suma actual: " + suma);
        } while (numero != 0);

        System.out.println("La suma total es: " + suma);
        scanner.close();
    }
}
