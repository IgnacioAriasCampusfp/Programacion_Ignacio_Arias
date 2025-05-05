package Hito;

import java.sql.*;

public class Controlador_Peliculas {
	//Realizamos la conexion de la base de datos instanciando a ConexionBBDD.
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	
		//Metodo para mostrar las peliculas junto a la categoria
	public void verPeliculas() {
        try {
        	

              //Creamos un Statement para usarlo despues
                Statement stmt = conexion.createStatement();
                //Si la conexion no es nula entonces realizaremos la consulta SQL
              if (conexion != null) {
            	  //Haremos la consulta y guardaremos los resultados
                    ResultSet rs = stmt.executeQuery("SELECT * FROM pelicula inner join categoria on pelicula.Categoria = categoria.id_categoria");
                    System.out.println("Mostrando Peliculas");
                    
                    //Realizaremos un bucle de la consulta hasta que no haya siguiente pelicula
                    while (rs.next()) {
                    	//Mostraremos por pantalla los datos que querramos indicando de que tipo son.
                        System.out.println("ID: " + rs.getInt("id_pelicula") + " Titulo: " + rs.getString("Titulo")+ " Valoraciones: "+rs.getString("Valoraciones")+ " Categoria: "+ rs.getString("Catg")+ " Año de Lanzamiento: "+rs.getDate("Lanzamiento"));
                    }
        }//Si nos da error se lo mostraremos por pantalla.
            }catch(SQLException e) {
                System.out.println("Error de selección: " + e.getMessage());
            }
        }
        
}


