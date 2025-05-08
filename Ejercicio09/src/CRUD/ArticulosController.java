package CRUD;

public class ArticulosController {
	Class_Articulos modelo = new Class_Articulos();

	
	public void crearArticulo(String nombre, double precio, int stock) {
		modelo.crearArticulo(nombre, precio, stock);
	}
	
	public void listarArticulos() {
		modelo.listarArticulos();
	}
	public void modificarArticulo(int id, String nombre, double precio, int stock) {
		modelo.modificarArticulo(id, nombre, precio, stock);		
	}
	public void eliminarArticulo(int id) {
		modelo.eliminarArticulo(id);
	}
}
