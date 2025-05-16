package Hito;

import java.sql.*;

public class Controlador_Peliculas {
	//Realizamos la conexion de la base de datos instanciando a ConexionBBDD.
	ConexionBBDD conexionBBDD = new ConexionBBDD();
	Connection conexion = conexionBBDD.conexion();
	
		//Metodo para mostrar las peliculas junto a la categoria
	public ResultSet verPeliculas() {
        try {
        	

              //Creamos un Statement para usarlo despues
                Statement stmt = conexion.createStatement();
                //Si la conexion no es nula entonces realizaremos la consulta SQL
              if (conexion != null) {
            	  //Haremos la consulta y guardaremos los resultados
                    ResultSet rs = stmt.executeQuery("SELECT * FROM pelicula inner join categoria on pelicula.Categoria = categoria.id_categoria");
                    System.out.println("Mostrando Peliculas");
                   

                    return rs;
                    
                    
                    //Realizaremos un bucle de la consulta hasta que no haya siguiente pelicula
                            }//Si nos da error se lo mostraremos por pantalla.
            }catch(SQLException e) {
                System.out.println("Error de selección: " + e.getMessage());
            }
		return null;
        }
    
    // Función para añadir película pidiendo los datos necesarios para añadirlo a la base de datos
    public void anadirPelicula(String titulo, String valoraciones, int id_categoria, Date lanzamiento) {
    	int id_nuevo = 0;
    	//Si nos devuelve vacio la conexion nos muestra este error
        if (conexion == null) {
            System.out.println("Error a la hora de conectar a la base de datos.");
            return;
        }

        try {
        	//Hacemos una consulta para comprobar el ultimo id añadido para hacerlo automaticamente            

          
            PreparedStatement nuevoIdStmt = conexion.prepareStatement("SELECT * FROM pelicula ORDER BY id_pelicula DESC LIMIT 1");
            ResultSet rs = nuevoIdStmt.executeQuery();
            if (rs.next()) {
            	id_nuevo = rs.getInt("id_pelicula") + 1;
            }
            //Hacemos una consulta de update con los datos proporcionados y el id obtenido a traves de la consulta anterios
            PreparedStatement insertStmt = conexion.prepareStatement(
                    "INSERT INTO pelicula (id_pelicula, titulo, valoraciones, Categoria, Lanzamiento) VALUES (?, ?, ?, ?, ?)");
            insertStmt.setInt(1, id_nuevo);
            insertStmt.setString(2, titulo);
            insertStmt.setString(3, valoraciones);
            insertStmt.setInt(4, id_categoria);
            insertStmt.setDate(5, lanzamiento);

            //Ejecutamos la consulta y nos mostrara un mensaje de exito
            insertStmt.executeUpdate();
            System.out.println("Película añadida correctamente.");
        } catch (SQLException e) {
            System.out.println("Error al añadir la película: " + e.getMessage());
        }
    }

    // Función para editar película que recibira los datos necesarios
    public void editarPelicula(int id_pelicula, String nuevoTitulo, String nuevasValoraciones, int nuevaCategoria, Date nuevaFecha) {
    	//Si nos devuelve vacio la conexion nos muestra este error
        if (conexion == null) {
            System.out.println("Error a la hora de conectar a la base de datos.");
            return;
        }

        try {
        	//Prepararemos la consulta para actualizar
            PreparedStatement updateStmt = conexion.prepareStatement(
                    "UPDATE pelicula SET titulo = ?, valoraciones = ?, Categoria = ?, lanzamiento = ? WHERE id_pelicula = ?");
            //Añadiremos los datos recibidos a la sentencia en orden
            updateStmt.setString(1, nuevoTitulo);
            updateStmt.setString(2, nuevasValoraciones);
            updateStmt.setInt(3, nuevaCategoria);
            updateStmt.setDate(4, nuevaFecha);
            updateStmt.setInt(5, id_pelicula);

            //Ejecutamos la consulta y lo guardamos
            int filas = updateStmt.executeUpdate();
            
            //Si encuentra algun resultado entonces significa que se a actualizado, su no encuentra nada entonces mostrara un mensaje que nos dira que no hay peliculas con ese ID

            if (filas > 0) {
                System.out.println("Película actualizada correctamente.");
            } else {
                System.out.println("No se encontró una película con ese ID.");
            }
        } catch (SQLException e) {
            System.out.println("Error al editar la película: " + e.getMessage());
        }
    }

    // Función para eliminar película
    public void eliminarPelicula(int id_pelicula) {
    	//Si nos devuelve vacio la conexion nos muestra este error
        if (conexion == null) {
            System.out.println("Error a la hora de conectar a la base de datos.");
            return;
        }

        try {
        	//Creamos una consulta para eliminar la pelicula seleccionada
            PreparedStatement deleteStmt = conexion.prepareStatement("DELETE FROM pelicula WHERE id_pelicula = ?");
            deleteStmt.setInt(1, id_pelicula);

            //Ejecutamos la consulta
            int filas = deleteStmt.executeUpdate();
            
            //Si encuentra algun resultado entonces significa que se a eliminado, su no encuentra nada entonces mostrara un mensaje que nos dira que no hay peliculas con ese ID
            if (filas > 0) {
            	
                System.out.println("Película eliminada correctamente.");
                
            } else {
            	
                System.out.println("No se encontró una película con ese ID.");
            }
        } catch (SQLException e) {
            System.out.println("Error al eliminar la película: " + e.getMessage());
        }
    }

    public void verCategoria() {
        
        // Si la conexión falla mensaje error
        if (conexion == null) {
            System.out.println("Error a la hora de conectar a la base de datos.");
            return;
        }
        try {
            // Creo la sentencia sql conectada a la db y le añadimos la Consulta que querramos realizar
            Statement stmt = conexion.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM categoria");


            System.out.println("Mostrando Categorías disponibles");

            //Mostraremos todas las categorias imprimiendo en la consola
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id_categoria") + " Categoría: " + rs.getString("catg"));
            }
            
            //Si falla algo a la hora de mostrar las categorias nos dara un mensaje
        } catch (SQLException e) {
            System.out.println("Error al recuperar categoria: " + e.getMessage());
        }
    }
    
    
}



