package CRUD;

import java.sql.Date;

public class VentasController {

	Class_Ventas modelo = new Class_Ventas();
	public void registrarVenta(int idCliente, int idArticulo, int cantidad, Date fecha) {
		modelo.registrarVenta(idCliente, idArticulo, cantidad, fecha);
	}
	public void listarVentas() {
		modelo.listarVentas();
	}
	public void modificarVenta(int idVenta, int idCliente, int idArticulo, int cantidad, Date fecha) {
		modelo.modificarVenta(idVenta, idCliente, idArticulo, cantidad, fecha);
	}
	public void eliminarVenta(int idVenta) {
		modelo.eliminarVenta(idVenta);
	}
}
