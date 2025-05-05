import java.util.*;
import java.io.*;
public class Main {
static Scanner scanner = new Scanner(System.in);
static ArrayList<Producto> productos = new ArrayList<Producto>();

	public static void main(String[] args) {
		Main mn = new Main();
		mn.menu();
		
	}
	public void menu() {
		int opcion;

        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Añadir nuevo producto");
            System.out.println("2. Mostrar todos los productos");
            System.out.println("0. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); 

            switch (opcion) {
                case 1:
                	aniadirProducto();
                    break;
                case 2:
                	mostrarProductos();
                    break;
                case 0:
                    System.out.println("Saliendo del programa.");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 0);
    }

	public static void aniadirProducto() {
		try {
            System.out.print("Nombre: ");
            String nombre = scanner.nextLine();
            System.out.print("Precio: ");
            double precio = scanner.nextDouble();
            System.out.print("Categoria: ");
            String cat = scanner.nextLine();
            scanner.nextLine(); 
            productos.add(new Producto(nombre, precio, cat));
           
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("productos.ser"));
            out.writeObject(productos);
            out.close();

            System.out.println("Producto añadido correctamente.");
            
            
        } catch (InputMismatchException e) {
            System.out.println("Error: Entrada no válida. Inténtalo de nuevo.");
            scanner.nextLine();
        } catch (IOException  e) {
            System.out.println("Error al guardar el empleado: " + e.getMessage());
        }
	}
	public static void mostrarProductos() {
		
		try {
			
        	ObjectInputStream in = new ObjectInputStream(new FileInputStream("productos.ser"));
			ArrayList<Producto> productos_rec = (ArrayList<Producto>) in.readObject();
            in.close();
            for(Producto pro : productos_rec) {
             System.out.println(pro.nombre + " Precio: " + pro.precio + " Categoria: " + pro.categoria);
                
            }
            

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error al leer productos: " + e.getMessage());
        }

	}
	
}
