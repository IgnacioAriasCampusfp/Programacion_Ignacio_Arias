package Hito;
import java.sql.Date;
import java.util.Scanner;

public class Programacion_H2_Parte2_3T_IgnacioArias {
	//Creamos instancias de scanner y del controlador de peliculas.
	static Scanner scanner = new Scanner(System.in);
	static Controlador_Peliculas controlador_p = new Controlador_Peliculas();
	
	public static void main(String[] args) {
		//Instanciamos Main y llamamos a Menú
		Programacion_H2_Parte2_3T_IgnacioArias main = new Programacion_H2_Parte2_3T_IgnacioArias();
		main.menu();
		
	}


	public  void menu() {
	       int opcion = 0;

	        do {
	        	try {	
	        	//Imprimimos el menu.
	            System.out.println("----- MENÚ ----- \n 1 – Ver películas \n 2 - Añadir Peliculas \n 3 - Eliminar Pelicula \n 4 - Actualizar Pelicula \n 5 – Salir");
	            System.out.print("Elige una opción: ");
	            //Le pedimos al usuario que no de una opcion.
	            opcion = scanner.nextInt();

	            switch (opcion) {
	            //Si el usuario no da la opcion 1 llamaremos a verPeliculas del Controlador
	            case 1:
                    
	            	controlador_p.verPeliculas();
                    break;
                    
                case 2:
                     Scanner scanner = new Scanner(System.in);
                     //Pediremos al usuario los datos de la pelicula para ingresarlo
                       
                        System.out.print("Introduce el título: ");
                        String titulo = scanner.nextLine();

                        System.out.print("Introduce las valoraciones: ");
                        String valoraciones = scanner.nextLine();
                        
                        //Imprimiremos las categorias para que el usuario pueda ver las categorias
                        controlador_p.verCategoria();
                        System.out.print("Introduce el ID de categoría : ");
                        

                        int id_categoria = scanner.nextInt();
                        scanner.nextLine(); 

                        System.out.print("Introduce la fecha de lanzamiento (YYYY-MM-DD): ");
                        String fechaStr = scanner.nextLine();
                        Date lanzamiento = Date.valueOf(fechaStr);

                        //Llamaremos al metodo añadir Pelicula con los datos proporcionados
                        controlador_p.anadirPelicula(titulo, valoraciones, id_categoria, lanzamiento);
                        break;
           
                case 3:
                    Scanner scanner4 = new Scanner(System.in);

                    //Pediremos el Id para eliminar
                    System.out.print("Introduce el ID de la película que deseas eliminar: ");
                    int id_Eliminar = scanner4.nextInt();

                    //
                    controlador_p.eliminarPelicula(id_Eliminar);
                    break;
                case 4:
                    Scanner scanner3 = new Scanner(System.in);
                    //Pediremos al usuario los datos de la pelicula para ingresarlo

                    System.out.print("Introduce el ID de la película que quieres editar: ");
                    int idEditar = scanner3.nextInt();
                    scanner3.nextLine(); 

                    System.out.print("Introduce el nuevo título: ");
                    String newTitulo = scanner3.nextLine();

                    System.out.print("Introduce las nuevas valoraciones: ");
                    String newValoraciones = scanner3.nextLine();

                    //Imprimiremos las categorias para que el usuario pueda ver las categorias
                    controlador_p.verCategoria();
                    System.out.print("Introduce el nuevo ID de categoría: ");
                    int newCategoria = scanner3.nextInt();
                    scanner3.nextLine();

                    System.out.print("Introduce la nueva fecha de lanzamiento (YYYY-MM-DD): ");
                    String newFechaStr = scanner3.nextLine();
                    Date newFecha = Date.valueOf(newFechaStr);

                    //Llamaremos al metodo editar Pelicula con los datos proporcionados
                    controlador_p.editarPelicula(idEditar, newTitulo, newValoraciones, newCategoria, newFecha);
                    break;

                case 5:
                    System.out.println("Terminando programa.");
                    
                    break;
	            }

	            System.out.println();
	            //Si da error nos saldrá un aviso del programa
	        	}catch(Exception e) {
	        	    System.out.println("Error: " + e.getMessage());
	        	    scanner.nextLine(); 
	        	}
	        	//Terminaremos el bucle si la opcion elegida es 2
	        } while (opcion != 5);

	        scanner.close();
	    }
	
	
	
	
	}


