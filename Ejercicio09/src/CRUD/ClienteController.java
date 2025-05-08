package CRUD;


public class ClienteController {
	
	Class_Cliente modelo = new Class_Cliente();
	
	
	public void anadirCliente(String nombre, String email, String telefono) {
		modelo.anadirCliente(nombre, email, telefono);
	}
	public void listarClientes() {
		modelo.listarClientes();
	}
	public void actualizarCliente(int id, String nombre, String email, String telefono) {
		modelo.actualizarCliente( id,  nombre,  email,  telefono);
	}
	public void eliminarCliente(int id) {
		modelo.eliminarCliente(id);
	}
	public void informePorCliente(int id) {
		modelo.informePorCliente(id);
	}

}
