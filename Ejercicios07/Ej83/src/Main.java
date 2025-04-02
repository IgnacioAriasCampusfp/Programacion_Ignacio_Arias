import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;


public class Main {

	public static void main(String[] args) {

		HashMap<Integer,Empleado> empleados = new HashMap<>();
		empleados.put(1,new EmpleadoFijo(1,"Juan",1523.1));
		empleados.put(2,new EmpleadoFijo(2,"Jhon",2647));
		empleados.put(3,new EmpleadoFijo(3,"Alberto",1200));
		empleados.put(4,new EmpleadoPorHoras(4,"Miguel",10,13));
		empleados.put(5,new EmpleadoPorHoras(5,"Nacho",4,20));
		empleados.put(6,new EmpleadoPorHoras(6,"Alex",25,7));
		
		Iterator<Map.Entry<Integer,Empleado>> it = empleados.entrySet().iterator();
		
		while(it.hasNext()) {
			
			Map.Entry<Integer,Empleado> entry = it.next();
			Empleado empleado = entry.getValue();
			System.out.println("Empleado: " + empleado.nombre + " - Salario mensual: " + empleado.calcularSalarioMensual());
		}

	}

}
