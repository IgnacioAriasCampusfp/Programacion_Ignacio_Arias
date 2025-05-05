import java.io.*;
import java.text.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		anadirFecha();
		
		
		  try {
			  BufferedReader buffer = new BufferedReader(new FileReader("historial.txt"));
				String linea;
			while ((linea = buffer.readLine()) != null) {
				  System.out.println(linea);
				  
			  }
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		
	}
	public static void anadirFecha() {
		
		try {
			Date fecha = new Date();
			DateFormat formato = DateFormat.getDateInstance(DateFormat.FULL);
			 DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
			 Date date = new Date();

			
			FileWriter escritor = new FileWriter("historial.txt", true);
			escritor.write(formato.format(fecha) + " " +  dateFormat.format(date) +"\n");
			escritor.close();

		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
