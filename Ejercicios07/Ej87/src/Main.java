	import java.util.*;
	
	public class Main {
	
		public static void main(String[] args) {
	
			ArrayList<Tarea> tareas = new ArrayList<>();
	        tareas.add(new TareaSimple("Lavar los platos", 2));
	        tareas.add(new TareaSimple("Hacer la compra", 1));
	        tareas.add(new TareaSimple("Sacar la basura", 3));
	
	        Collections.sort(tareas);
	        
	        for(Tarea tarea : tareas) {
	        	tarea.ejecutar();
	       }
		}
	
	}
