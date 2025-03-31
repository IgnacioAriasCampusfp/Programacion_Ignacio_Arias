import java.util.ArrayList;
import java.util.Iterator;

public class Main {

	public static void main(String[] args) {

		
		ArrayList<String> frutas = new ArrayList<>();
		frutas.add("Pera");
		frutas.add("Fresa");
		frutas.add("Manzana");
		frutas.add("Melón");
		System.out.println(frutas);
		Iterator<String> it = frutas.iterator();
		while (it.hasNext()) {
		    String f = it.next();
		    if (f.equals("Manzana")) {
		        it.remove(); 
		    }
		}
		System.out.println(frutas);
		
	}

}
