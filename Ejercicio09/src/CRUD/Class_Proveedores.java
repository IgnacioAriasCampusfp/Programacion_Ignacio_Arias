package CRUD;

import java.sql.Connection;
import java.sql.*;

public class Class_Proveedores {
	
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	
	public void crearProveedor(String nombre, String cif, String telefono) {
	    try{
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "INSERT INTO Proveedores (nombre, cif, telefono) VALUES (?, ?, ?)");
	        stmt.setString(1, nombre);
	        stmt.setString(2, cif);
	        stmt.setString(3, telefono);
	        stmt.executeUpdate();
	        System.out.println("Proveedor creado con éxito.");
	    } catch (SQLException e) {
	        System.err.println("Error al crear proveedor: " + e.getMessage());
	    }
	}

	public void listarProveedores() {
	    try {
	    	Statement stmt = conexion.createStatement();
	         ResultSet rs = stmt.executeQuery("SELECT * FROM Proveedores");
	        while (rs.next()) {
	            System.out.printf("ID: %d | Nombre: %s | CIF: %s | Teléfono: %s\n",
	                    rs.getInt("id_proveedor"), rs.getString("nombre"),
	                    rs.getString("cif"), rs.getString("telefono"));
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al listar proveedores: " + e.getMessage());
	    }
	}

	public void modificarProveedor(int id, String nombre, String cif, String telefono) {
	    try {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "UPDATE Proveedores SET nombre=?, cif=?, telefono=? WHERE id_proveedor=?");
	        stmt.setString(1, nombre);
	        stmt.setString(2, cif);
	        stmt.setString(3, telefono);
	        stmt.setInt(4, id);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) System.out.println("Proveedor modificado.");
	        else System.out.println("Proveedor no encontrado.");
	    } catch (SQLException e) {
	        System.err.println("Error al modificar proveedor: " + e.getMessage());
	    }
	}

	public void eliminarProveedor(int id) {
	    try {
	    	PreparedStatement stmt = conexion.prepareStatement(
		            "DELETE FROM Proveedores WHERE id_proveedor=?");
	        stmt.setInt(1, id);
	        int filas = stmt.executeUpdate();
	        if (filas > 0) System.out.println("Proveedor eliminado.");
	        else System.out.println("Proveedor no encontrado.");
	    } catch (SQLException e) {
	        System.err.println("Error al eliminar proveedor: " + e.getMessage());
	    }
	}

}
