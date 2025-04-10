import java.util.*;

public class Main {
	ArrayList<Vehiculo> vehiculos = new ArrayList<>();
	
	Scanner scan = new Scanner(System.in);
	
	
	public static void main(String[] args) {
	
		Main main = new Main();
		main.añadirVehiculo();
		main.menu();
		
		
	}
	public void añadirVehiculo() {
		vehiculos.add(new Autobus("897213BDS",1998,45,true));
		vehiculos.add(new Autobus("654132MDK",2025,50,true));
		vehiculos.add(new Autobus("312654JDW",2012,35,true));
		vehiculos.add(new Furgoneta("789456PLD",2025,5,"Alimentos"));
		vehiculos.add(new Furgoneta("465123BDX",1950,5,"Mercancia ilegal"));
		vehiculos.add(new Furgoneta("984512SSS",2020,5,"Inmigrantes"));


	}
	
	public void menu() {
		int opcion;
		do {
			System.out.println("1 - Añadir un nuevo vehículo 2 - Mostrar todos los vehículos 3 - Buscar un vehículo por su código 4 - Eliminar un vehículo dado su código. 5 - Salir");
			opcion = scan.nextInt();
			switch(opcion) {
			case 1:
				this.menuVehiculos();
				break;
			case 2:
				this.mostrarDatos();
				break;
			case 3:
				System.out.println("Ingrese el codigo del vehiculo para buscarlo");
				scan.nextLine();
				String codigo = scan.nextLine();
				this.buscarVehiculo(codigo);
				break;
			case 4:
				System.out.println("Ingrese el codigo del vehiculo para eliminarlo");
				scan.nextLine();
				String codigoe = scan.nextLine();
				this.eliminarVehiculo(codigoe);
				break;
			case 5:
				System.exit(0);
				break;
			default:
				System.out.println("Opcion no valida");
				break;
			}
			
			
			
		}while(opcion != 5);
		
		
		
		
	}
	public void menuVehiculos() {
		
		int opcion;
		do {
			System.out.println("1 - Añadir un Autobús 2 - Añadir una Furgoneta 3 - Volver");
			opcion = scan.nextInt();
			switch(opcion) {
			case 1:
				this.agregarAutobus();
				break;
			case 2:
				this.agregarFurgonetas();
				break;
			case 3:
				
				break;
			
			default:
				System.out.println("Opcion no valida");
				break;
			}
			
			
			
		}while(opcion != 3);

	}
	public void agregarAutobus() {
		try {

			scan.nextLine();
			
			System.out.println("Codigo del vehiculo: ");
			String codigo = scan.nextLine();
			
			System.out.println("Año de adquisicion");
			int anio = scan.nextInt();
			
			scan.nextLine();
			System.out.println("Numero de plazas: ");
			int plaza = scan.nextInt();
			
			System.out.println("Adaptado para personas discapacidadas True / False");
			boolean adaptado = scan.nextBoolean();
			scan.nextLine();

			vehiculos.add(new Autobus(codigo, anio, plaza, adaptado));
			System.out.println("Autobus con codigo de vehiculo: " + codigo + " a sido registrado" );

			}catch (Exception e) {
			System.out.println("Error a la hora de introducir datos intente de nuevo.");
			}
		
	}
	public void agregarFurgonetas() {
		try {

			scan.nextLine();
			
			System.out.println("Codigo del vehiculo: ");
			String codigo = scan.nextLine();
			
			System.out.println("Año de adquisicion");
			int anio = scan.nextInt();
			
			scan.nextLine();
			System.out.println("Numero de plazas: ");
			int plaza = scan.nextInt();
			
			System.out.println("A que tipo de carga esta destinado: ");
			String tipo = scan.nextLine();
			scan.nextLine();

			vehiculos.add(new Furgoneta(codigo, anio, plaza, tipo));
			System.out.println("Autobus con codigo de vehiculo: " + codigo + " a sido registrado" );

			}catch (Exception e) {
			System.out.println("Error a la hora de introducir datos intente de nuevo.");
			}
		
	}
	public void mostrarDatos() {
		
		for(Vehiculo vehiculo : vehiculos) {
			vehiculo.mostrar();
		}
	}
	public void buscarVehiculo(String codigo) {
		boolean encontrado = false;
		for(Vehiculo vehiculo : vehiculos) {
			if (vehiculo.codigo == codigo) {
				vehiculo.mostrar();
				encontrado = true;
				break;
			}
			
		}
		if(encontrado != true) {
			System.out.println("Vehiculo no encontrado");
		}
	}
	public void eliminarVehiculo(String codigo) {
	    Iterator<Vehiculo> iterator = vehiculos.iterator();
	    while (iterator.hasNext()) {
	        Vehiculo vehiculo = iterator.next();
	        if (vehiculo.codigo.equals(codigo)) {
	            iterator.remove(); 
	            break; 
	        }
	    }
	}
}
