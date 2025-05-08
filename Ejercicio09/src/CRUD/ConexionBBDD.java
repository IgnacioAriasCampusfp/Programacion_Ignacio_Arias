package CRUD;

import java.sql.*;
public class ConexionBBDD {

	
	
	
	public Connection conexion() {
		try {
			//Hazemos la conexion a la base de datos por el puerto 33 ya que lo hemos tenido que cambiar por problemas
			Connection miConexion = DriverManager.getConnection("jdbc:mysql://localhost:33/javapoo", "root", "");
			//Devolvemos la conexion
			return miConexion;
			
			//Si da error en algun paso nos devolvera nulo
		}catch(Exception e) {
			return null;
		}
		
	}
	
}
