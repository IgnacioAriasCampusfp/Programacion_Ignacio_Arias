import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {

		ArrayList<Producto> productos = new ArrayList<>();
		productos.add(new Producto("Carne picada",25));
		productos.add(new Producto("Salchichon",15));
		productos.add(new Producto("Jamon iberico",75));
		productos.add(new Producto("Chorizo",50));
		productos.add(new Producto("Fuet",49));

		for(Producto producto : productos) {
			if(producto.precio >= 50) {
				System.out.println(producto.nombre + " " + producto.precio + "€");
			}
		}
		
	}

}
