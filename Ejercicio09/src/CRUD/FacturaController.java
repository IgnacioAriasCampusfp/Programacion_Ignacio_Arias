package CRUD;

import java.sql.Date;

public class FacturaController {
	Class_Factura modelo = new Class_Factura();
	
	public void crearFactura(int idProveedor, Date fecha, double total) {
		modelo.crearFactura(idProveedor, fecha, total);
	}
	public void listarFacturas() {
		modelo.listarFacturas();
	}
	public void modificarFactura(int idFactura, int idProveedor, Date fecha, double total) {
		modelo.modificarFactura(idFactura, idProveedor, fecha, total);
	}
	public void eliminarFactura(int idFactura) {
		modelo.eliminarFactura(idFactura);
	}
}
