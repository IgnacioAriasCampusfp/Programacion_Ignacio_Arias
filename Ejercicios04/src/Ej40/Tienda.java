package Ej40;
import java.util.ArrayList;
import java.util.Scanner;

public class Tienda {

	ArrayList<Producto> productos = new ArrayList<Producto>();
	Scanner scanner = new Scanner(System.in);

	public void agregarProducto() {
		
			System.out.println("Introduzca un nombre del nuevo producto ");
			String nombre = scanner.nextLine();
				System.out.println("Introduzca el precio del producto");
				double precio = scanner.nextDouble();
				System.out.println("Cuanto stock hay de este producto");
				int stock = scanner.nextInt();
				Producto producto = new Producto(nombre,precio,stock);
				productos.add(producto);
		}

		
		
			
	public void mostrarProductos() {
			for (Producto producto : productos) {
	            System.out.println(producto);
	        
            }
		}	
	
	}

