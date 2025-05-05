import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;


public class Main {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		try {
			FileWriter escritor = new FileWriter("mensaje.txt");
			System.out.println("Primera frase: ");
			String texto = scan.nextLine();
			escritor.write(texto + "\n");
			System.out.println("Segunda frase: ");
			texto = scan.nextLine();
			escritor.write(texto + "\n");
			System.out.println("Guardado correctamente");
			escritor.close();
			
			BufferedReader buffer = new BufferedReader(new FileReader("mensaje.txt"));
			String linea;
			
			  while ((linea = buffer.readLine()) != null) {
				  System.out.println(linea);
				  
			  }
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
