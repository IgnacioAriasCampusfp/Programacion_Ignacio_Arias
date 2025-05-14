package CRUD;
import java.sql.*;


public class Class_Cliente {
	
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	
	public void anadirCliente(String nombre, String email, String telefono) {
		try  {
			PreparedStatement stmt = conexion.prepareStatement(
	                "INSERT INTO Clientes (nombre, email, telefono) VALUES (?, ?, ?)");
            stmt.setString(1, nombre);
            stmt.setString(2, email);
            stmt.setString(3, telefono);
            stmt.executeUpdate();
            System.out.println("Cliente creado con éxito.");
        } catch (SQLException e) {
            System.err.println("Error al crear cliente: " + e.getMessage());
        }

	}
	public void listarClientes() {
		
		try{
			Statement stmt = conexion.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM Clientes");
	            while (rs.next()) {
	                System.out.printf("ID: %d | Nombre: %s | Email: %s | Teléfono: %s\n",
	                        rs.getInt("id_cliente"), rs.getString("nombre"),
	                        rs.getString("email"), rs.getString("telefono"));
	            }
	        } catch (SQLException e) {
	            System.err.println("Error al listar clientes: " + e.getMessage());
	        }

	}
	public void actualizarCliente(int id, String nombre, String email, String telefono) {
		try {
			PreparedStatement stmt = conexion.prepareStatement(
	                "UPDATE Clientes SET nombre=?, email=?, telefono=? WHERE id_cliente=?");
            stmt.setString(1, nombre);
            stmt.setString(2, email);
            stmt.setString(3, telefono);
            stmt.setInt(4, id);
            int filas = stmt.executeUpdate();
            if (filas > 0) { 
            	System.out.println("Cliente modificado.");
            	}
            else System.out.println("Cliente no encontrado.");
        } catch (SQLException e) {
            System.err.println("Error al modificar cliente: " + e.getMessage());
        }

	}
	public void eliminarCliente(int id) {
		try{
			PreparedStatement stmt = conexion.prepareStatement(
	                "DELETE FROM Clientes WHERE id_cliente=?");
            stmt.setInt(1, id);
            int filas = stmt.executeUpdate();
            if (filas > 0) System.out.println("Cliente eliminado.");
            else System.out.println("Cliente no encontrado.");
        } catch (SQLException e) {
            System.err.println("Error al eliminar cliente: " + e.getMessage());
        }

	}
	public void informePorCliente(int idCliente) {
        String query = """
            SELECT c.nombre AS cliente, a.nombre AS articulo, v.cantidad, v.fecha_venta, 
                   (v.cantidad * a.precio_unitario) AS subtotal
            FROM Ventas v
            JOIN Clientes c ON v.id_cliente = c.id_cliente
            JOIN Articulos a ON v.id_articulo = a.id_articulo
            WHERE v.id_cliente = ?;
        """;

        try{
        	PreparedStatement stmt = conexion.prepareStatement(query);
            stmt.setInt(1, idCliente);
            ResultSet rs = stmt.executeQuery();

            double total = 0;
            System.out.println("\n--- INFORME DE COMPRAS ---");
            while (rs.next()) {
                String cliente = rs.getString("cliente");
                String articulo = rs.getString("articulo");
                int cantidad = rs.getInt("cantidad");
                Date fecha = rs.getDate("fecha_venta");
                double subtotal = rs.getDouble("subtotal");
                total += subtotal;

                System.out.printf("Cliente: %s | Artículo: %s | Cantidad: %d | Fecha: %s | Subtotal: %.2f\n",
                        cliente, articulo, cantidad, fecha, subtotal);
            }
            System.out.printf("TOTAL GASTADO: %.2f\n", total);
        } catch (SQLException e) {
            System.err.println("Error al generar informe: " + e.getMessage());
        }
    }

}
