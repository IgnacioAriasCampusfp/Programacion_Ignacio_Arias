
public class Factura implements Imprimible {

	
	public void imprimir() {
		System.out.println("==========================================\r\n"
				+ "            FACTURA ELECTRÓNICA\r\n"
				+ "==========================================\r\n"
				+ "Número de Factura: 2025-00345\r\n"
				+ "Fecha: 27/03/2025  -  Hora: 14:35:22\r\n"
				+ "Cliente: Juan Pérez\r\n"
				+ "------------------------------------------\r\n"
				+ "Descripción           Cant.    P. Unit    Total\r\n"
				+ "------------------------------------------\r\n"
				+ "Producto A              2      15.00      30.00\r\n"
				+ "Producto B              1      25.50      25.50\r\n"
				+ "Producto C              3      10.00      30.00\r\n"
				+ "------------------------------------------\r\n"
				+ "Subtotal:                          85.50\r\n"
				+ "IVA (12%):                        10.26\r\n"
				+ "Total a Pagar:                     95.76\r\n"
				+ "------------------------------------------\r\n"
				+ "Método de Pago: Tarjeta de Crédito\r\n"
				+ "Atendido por: María López\r\n"
				+ "==========================================\r\n"
				+ "        ¡Gracias por su compra!\r\n"
				+ "==========================================\r\n"
				+ "");
		
	}

}
