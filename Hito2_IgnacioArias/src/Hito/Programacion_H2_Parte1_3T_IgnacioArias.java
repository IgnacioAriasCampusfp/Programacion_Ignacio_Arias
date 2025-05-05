package Hito;
import java.util.Scanner;

public class Programacion_H2_Parte1_3T_IgnacioArias {
	//Creamos instancias de scanner y del controlador de peliculas.
	static Scanner scanner = new Scanner(System.in);
	static Controlador_Peliculas controlador_p = new Controlador_Peliculas();
	
	public static void main(String[] args) {
		//Instanciamos Main y llamamos a Menú
		Programacion_H2_Parte1_3T_IgnacioArias main = new Programacion_H2_Parte1_3T_IgnacioArias();
		main.menu();
		
	}


	public  void menu() {
	       int opcion = 0;

	        do {
	        	try {	
	        	//Imprimimos el menu.
	            System.out.println("----- MENÚ ----- \n 1 – Ver películas \n 2 – Salir");
	            System.out.print("Elige una opción: ");
	            //Le pedimos al usuario que no de una opcion.
	            opcion = scanner.nextInt();

	            switch (opcion) {
	            //Si el usuario no da la opcion 1 llamaremos a verPeliculas del Controlador
	                case 1:
	                	controlador_p.verPeliculas();
	                    break;
	                 //Si nos da la opcion 2 saldremos del programa
	                case 2:
	                    System.out.println("Saliendo del programa.");
	                    break;
	                //Si nos da una opcion que no está en las opciones nos da un error
	                default:
	                    System.out.println("Opción no válida. Intenta de nuevo.");
	                    break;
	            }

	            System.out.println();
	            //Si da error nos saldrá un aviso del programa
	        	}catch(Exception e) {
	        	    System.out.println("Error: " + e.getMessage());
	        	    scanner.nextLine(); 
	        	}
	        	//Terminaremos el bucle si la opcion elegida es 2
	        } while (opcion != 2);

	        scanner.close();
	    }
	
	
	
	
	}


