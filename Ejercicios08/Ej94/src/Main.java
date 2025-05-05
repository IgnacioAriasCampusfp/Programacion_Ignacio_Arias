import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		
		while(true) {
			try {
				System.out.println("Introduzca el nombre del archivo: ");
				String archivo = scan.nextLine() + ".txt";
				BufferedReader buffer =  new BufferedReader(new FileReader(archivo));
				String linea;
				while((linea = buffer.readLine()) != null) {
								System.out.println(linea);
				}	
				
			}catch(IOException e) {
				e.printStackTrace();
			}
		}
	
		
	

		
	}

}
