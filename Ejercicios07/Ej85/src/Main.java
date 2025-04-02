import java.util.ArrayList;
import java.util.HashMap;

public class Main {

	public static void main(String[] args) {

		HashMap<String, ArrayList<Item>> items = new HashMap<>();
		items.put("Libro", new ArrayList<>());
	    items.put("Electronico", new ArrayList<>());
	        
		items.get("Libro").add(new Libro("El camino de los reyes"));
        items.get("Libro").add(new Libro("Palabras radiantes"));
        items.get("Libro").add(new Libro("Juramentada"));
        items.get("Libro").add(new Libro("Ritmo de la guerra"));
        items.get("Libro").add(new Libro("Viento y Verdad"));
        items.get("Libro").add(new Libro("Peppa Pig y sus amigos"));

        items.get("Electronico").add(new Electronico("Xiaomi"));
        items.get("Electronico").add(new Electronico("Samsung"));
        items.get("Electronico").add(new Electronico("Nespresso"));
        items.get("Electronico").add(new Electronico("Bandai"));

        for (String categoria : items.keySet()) {
            System.out.println("Categoría: " + categoria);
            for (Item item : items.get(categoria)) {
                System.out.println(" - " + item.describir());            }
        }

		

	}

}
