package CRUD;

import java.sql.Connection;
import java.sql.*;

public class Class_Factura {
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	
	public void crearFactura(int idProveedor, Date fecha, double total) {
	    try  {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "INSERT INTO Facturas_Recibidas (id_proveedor, fecha, total) VALUES (?, ?, ?)");
	        stmt.setInt(1, idProveedor);
	        stmt.setDate(2, fecha);
	        stmt.setDouble(3, total);
	        stmt.executeUpdate();
	        System.out.println("Factura registrada.");
	    } catch (SQLException e) {
	        System.err.println("Error al crear factura: " + e.getMessage());
	    }
	}

	public void listarFacturas() {
	    try  {
	    	Statement stmt = conexion.createStatement();
	         ResultSet rs = stmt.executeQuery("SELECT * FROM Facturas_Recibidas");
	        while (rs.next()) {
	            System.out.printf("ID: %d | Proveedor: %d | Fecha: %s | Total: %.2f\n",
	                    rs.getInt("id_factura"), rs.getInt("id_proveedor"),
	                    rs.getDate("fecha"), rs.getDouble("total"));
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al listar facturas: " + e.getMessage());
	    }
	}

	public void modificarFactura(int idFactura, int idProveedor, Date fecha, double total) {
	    try {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "UPDATE Facturas_Recibidas SET id_proveedor = ?, fecha = ?, total = ? WHERE id_factura = ?");
	        stmt.setInt(1, idProveedor);
	        stmt.setDate(2, fecha);
	        stmt.setDouble(3, total);
	        stmt.setInt(4, idFactura);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) {
	            System.out.println("Factura modificada.");
	        } else {
	            System.out.println("Factura no encontrada.");
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al modificar factura: " + e.getMessage());
	    }
	}

	public void eliminarFactura(int idFactura) {
	    try  {
	    	PreparedStatement stmt = conexion.prepareStatement("DELETE FROM Facturas_Recibidas WHERE id_factura = ?");
	        stmt.setInt(1, idFactura);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) {
	            System.out.println("Factura eliminada.");
	        } else {
	            System.out.println("Factura no encontrada.");
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al eliminar factura: " + e.getMessage());
	    }
	}

}
