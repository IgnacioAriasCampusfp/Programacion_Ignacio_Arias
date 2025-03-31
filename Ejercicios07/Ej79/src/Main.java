import java.util.*;
public class Main {

	public static void main(String[] args) {

		ArrayList<String> nombres = new ArrayList<>();
		nombres.add("juan");
		nombres.add("pablo");
		nombres.add("miguel");
		
		for(String nombre : nombres) {
			
			System.out.println(nombre.toUpperCase());
		}
		
		
	}

}
