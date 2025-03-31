import java.util.HashMap;

public class Main {

	public static void main(String[] args) {
		HashMap<String,Integer> persona = new HashMap<>();
		persona.put("Ana", 32);
		persona.put("Juan", 42);
		System.out.println(persona.get("Ana"));
		System.out.println(persona.get("Juan"));

		
	}

}
