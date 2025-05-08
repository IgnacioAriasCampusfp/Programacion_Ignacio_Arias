package CRUD;

import java.sql.*;

public class Class_Ventas {
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();


	public void registrarVenta(int idCliente, int idArticulo, int cantidad, Date fecha) {
	    try{
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "INSERT INTO Ventas (id_cliente, id_articulo, cantidad, fecha_venta) VALUES (?, ?, ?, ?)");
	        stmt.setInt(1, idCliente);
	        stmt.setInt(2, idArticulo);
	        stmt.setInt(3, cantidad);
	        stmt.setDate(4, fecha);
	        stmt.executeUpdate();
	        System.out.println("Venta registrada.");
	    } catch (SQLException e) {
	        System.err.println("Error al registrar venta: " + e.getMessage());
	    }
	}

	public void listarVentas() {
	    try  {
	    	Statement stmt = conexion.createStatement();
	         ResultSet rs = stmt.executeQuery("SELECT * FROM Ventas");
	        while (rs.next()) {
	            System.out.printf("ID: %d | Cliente: %d | Artículo: %d | Cantidad: %d | Fecha: %s\n",
	                    rs.getInt("id_venta"), rs.getInt("id_cliente"),
	                    rs.getInt("id_articulo"), rs.getInt("cantidad"),
	                    rs.getDate("fecha_venta"));
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al listar ventas: " + e.getMessage());
	    }
	}

	public void modificarVenta(int idVenta, int idCliente, int idArticulo, int cantidad, Date fecha) {
	    try {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "UPDATE Ventas SET id_cliente = ?, id_articulo = ?, cantidad = ?, fecha_venta = ? WHERE id_venta = ?");
	        stmt.setInt(1, idCliente);
	        stmt.setInt(2, idArticulo);
	        stmt.setInt(3, cantidad);
	        stmt.setDate(4, fecha);
	        stmt.setInt(5, idVenta);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) {
	            System.out.println("Venta modificada.");
	        } else {
	            System.out.println("Venta no encontrada.");
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al modificar venta: " + e.getMessage());
	    }
	}

	public void eliminarVenta(int idVenta) {
	    try{
	    	PreparedStatement stmt = conexion.prepareStatement("DELETE FROM Ventas WHERE id_venta = ?");
	        stmt.setInt(1, idVenta);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) {
	            System.out.println("Venta eliminada.");
	        } else {
	            System.out.println("Venta no encontrada.");
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al eliminar venta: " + e.getMessage());
	    }
	}

}
