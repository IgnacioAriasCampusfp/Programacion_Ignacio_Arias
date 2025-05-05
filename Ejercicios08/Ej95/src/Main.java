import java.io.*;
import java.util.*;
public class Main {
static Scanner scanner = new Scanner(System.in);
static ArrayList<Empleado> empleados = new ArrayList<Empleado>();

	public static void main(String[] args) {
		
		Main mn = new Main();
		mn.menu();
		
	}

	public void menu() {
		int opcion;

        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Añadir nuevo empleado");
            System.out.println("2. Mostrar todos los empleados");
            System.out.println("0. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); 

            switch (opcion) {
                case 1:
                    añadirEmpleado();
                    break;
                case 2:
                	mostrarEmpleados();
                    break;
                case 0:
                    System.out.println("Saliendo del programa.");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 0);
    }
	
	public static void añadirEmpleado() {
        try {
            System.out.print("Nombre: ");
            String nombre = scanner.nextLine();
            System.out.print("Edad: ");
            int edad = scanner.nextInt();
            System.out.print("Salario: ");
            double salario = scanner.nextDouble();
            scanner.nextLine(); 
            empleados.add(new Empleado(nombre, edad, salario));
           
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("empleados.ser"));
            out.writeObject(empleados);
            out.close();

            System.out.println("Empleado añadido correctamente.");
            
            
        } catch (InputMismatchException e) {
            System.out.println("Error: Entrada no válida. Inténtalo de nuevo.");
            scanner.nextLine();
        } catch (IOException  e) {
            System.out.println("Error al guardar el empleado: " + e.getMessage());
        }
    }
	@SuppressWarnings("unchecked")
	public static void mostrarEmpleados() {
        try {
        	ObjectInputStream in = new ObjectInputStream(new FileInputStream("empleados.ser"));
			ArrayList<Empleado> empleados_recuperados = (ArrayList<Empleado>) in.readObject();
            in.close();
            for(Empleado emp : empleados_recuperados) {
            	System.out.println(emp.nombre + " Edad: " +emp.edad + " Salario: " + emp.salario);
            }

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error al leer empleados: " + e.getMessage());
        }
    }
}

