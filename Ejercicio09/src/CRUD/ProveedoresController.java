package CRUD;


public class ProveedoresController {
	Class_Proveedores modelo = new Class_Proveedores();
	
	
	
	public void crearProveedor(String nombre, String cif, String telefono) {
		modelo.crearProveedor(nombre, cif, telefono);
	}
	public void listarProveedores() {
		modelo.listarProveedores();
	}
	public void modificarProveedor(int id, String nombre, String cif, String telefono) {
		modelo.modificarProveedor(id, nombre, cif, telefono);
	}
	public void eliminarProveedor(int id) {
		modelo.eliminarProveedor(id);
	}
}
