package CRUD;

import java.sql.*;

public class Class_Articulos {
	
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	

	
	public void crearArticulo(String nombre, double precio, int stock) {
	    try  {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "INSERT INTO Articulos (nombre, precio_unitario, stock) VALUES (?, ?, ?)");
	        stmt.setString(1, nombre);
	        stmt.setDouble(2, precio);
	        stmt.setInt(3, stock);
	        stmt.executeUpdate();
	        System.out.println("Artículo creado.");
	    } catch (SQLException e) {
	        System.err.println("Error al crear artículo: " + e.getMessage());
	    }
	}

	public void listarArticulos() {
	    try  {
	    	Statement stmt = conexion.createStatement();
	         ResultSet rs = stmt.executeQuery("SELECT * FROM Articulos");
	        while (rs.next()) {
	            System.out.printf("ID: %d | Nombre: %s | Precio: %.2f | Stock: %d\n",
	                    rs.getInt("id_articulo"), rs.getString("nombre"),
	                    rs.getDouble("precio_unitario"), rs.getInt("stock"));
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al listar artículos: " + e.getMessage());
	    }
	}

	public void modificarArticulo(int id, String nombre, double precio, int stock) {
	    try  {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "UPDATE Articulos SET nombre=?, precio_unitario=?, stock=? WHERE id_articulo=?");
	        stmt.setString(1, nombre);
	        stmt.setDouble(2, precio);
	        stmt.setInt(3, stock);
	        stmt.setInt(4, id);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) System.out.println("Artículo modificado.");
	        else System.out.println("Artículo no encontrado.");
	    } catch (SQLException e) {
	        System.err.println("Error al modificar artículo: " + e.getMessage());
	    }
	}

	public void eliminarArticulo(int id) {
	    try  {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "DELETE FROM Articulos WHERE id_articulo=?");
	        stmt.setInt(1, id);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) System.out.println("Artículo eliminado.");
	        else System.out.println("Artículo no encontrado.");
	    } catch (SQLException e) {
	        System.err.println("Error al eliminar artículo: " + e.getMessage());
	    }
	}


}
