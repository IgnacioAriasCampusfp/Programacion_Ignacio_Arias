import java.io.Serializable;

public class Producto implements Serializable {
	String nombre;
	double precio;
	String categoria;
	
	
	public Producto(String nombre, double precio, String categoria) {
		this.nombre = nombre;
		this.precio = precio;
		this.categoria = categoria;
	}
}
