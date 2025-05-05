import java.io.*;

public class Main {

	public static void main(String[] args) {
		int total = 0;
		try {
			BufferedReader buffer =  new BufferedReader(new FileReader("numeros.txt"));
			String linea;
			
		
				while((linea = buffer.readLine()) != null) {
					int numero = Integer.parseInt(linea);
					total = total + numero;
					
				}
				System.out.println(total);
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
