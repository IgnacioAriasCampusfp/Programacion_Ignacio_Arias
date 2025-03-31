import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {

		
		ArrayList<String> tareas = new ArrayList<String>();
		tareas.add("Hacer la compra.");
		tareas.add("Limpiar la cocina.");
		tareas.add("Comer.");
		System.out.println(tareas);
		tareas.remove(0);
		System.out.println(tareas);
		
		
	}

}
