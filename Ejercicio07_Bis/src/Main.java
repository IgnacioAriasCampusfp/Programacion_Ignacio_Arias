import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		ArrayList<BibliotecaEscolar> materiales = new ArrayList<>();
		materiales.add(new Libro("L001", "Programación en Java", 2021, "Ana García", 350));
		materiales.add(new Revista("R010", "Ciencia Escolar", 2023, 12, true));
		materiales.add(new Libro("L002", "Matemáticas Básicas", 2019, "Carlos Ruiz", 200));
		materiales.add(new Revista("R011", "Arte y Diseño", 2022, 7, false));
		
		Scanner agregar = new Scanner (System.in);
		
		 System.out.println("¿Quieres añadir un 'Libro' o una 'Revista'?");
	     System.out.println("Ingresa 1 si quieres añadir un libro, o ingresa 2 si quieres añadir una revista:");
	     int opcion = agregar.nextInt();
	     agregar.nextLine();
		
	     System.out.print("Ingresa el código: ");
	     String codigo = agregar.nextLine();
	    
	     boolean existe = false;
	     for (BibliotecaEscolar material : materiales) {
	    	 if (material.getCodigo().equalsIgnoreCase(codigo)) {
	    		 existe = true;
	    		 break;
	    	 }
	     }
	    
	     if (existe) {
	    	 System.out.println("Ya existe un material con ese código. No se ha añadido.");
	    	 return;
	     }
		
	     System.out.print("Ingresa el título: ");
	     String titulo = agregar.nextLine();
	     System.out.print("Ingresa el año de publicación: ");
	     int anioPublicacion = agregar.nextInt();
	     agregar.nextLine();
	    
	     if(opcion == 1) {
	    	 System.out.println("Ingresa el nombre del autor:");
	    	 String autor = agregar.nextLine();
				
	    	 System.out.println("Ingresa el numero de paginas del libro:");
	    	 int paginas = agregar.nextInt();
				
	    	 materiales.add(new Libro(codigo, titulo, anioPublicacion, autor, paginas));
	    	 System.out.println("¡Material añadido correctamente!");
	     }
	     else if(opcion == 2) {
	    	 System.out.println("Ingresa el numero de la revista:");
	    	 int numero = agregar.nextInt();
	    	 agregar.nextLine();
				
	    	 System.out.print("La revista es mensual (true/false): ");
            boolean esMensual = Boolean.parseBoolean(agregar.nextLine());
           
            materiales.add(new Revista(codigo, titulo, anioPublicacion, numero, esMensual));
            System.out.println("¡Material añadido correctamente!");
	     }
	     else {
	            System.out.println("Selecciona una de las 2 opciones válidas.");
	        }
	}

}
