package Hito;

//Importar java.util para el uso de arraylist y scanner
import java.util.*;
public class Programación_H1_Parte_1_3doT_IgnacioArias {
	//Creamos instancia de scanner y de el arrayList de animal
	Scanner scan = new Scanner(System.in);	
	static ArrayList<Animal> animales = new ArrayList<>();
	
	public static void main(String[] args) {
		
		//Instaciamos esta clase para llamar al menu
		Programación_H1_Parte_1_3doT_IgnacioArias hito = new Programación_H1_Parte_1_3doT_IgnacioArias();
		hito.menu();
		
	}

	//Metodo que nos hace interactuar con los metodos del codigo
public void menu() {
		try {
			
			int opcion;

			do {
				//Mostramos las opciones y le pedimos que ingrese una opcion
				System.out.println("1 - Agregar perro 2 - Agregar gato 3 - Buscar animales 4 - Salir");
				opcion = scan.nextInt();
					switch (opcion) {
					case 1:
						//llamamos a agregarPerro si la opcion elegida es 1
						this.agregarPerro();
						break;
					case 2:
						//llamamos a agregarGato si la opcion elegida es 2
						this.agregarGato();
						break;
					case 3:
						//llamamos a mostrarAnimales con un paso antes que es pedirle el numero de chip del animal buscado

						System.out.println("Numero del animal buscado");
						int num = scan.nextInt();
						this.mostrarAnimales(num);
						break;
					case 4:
						//Salimos del codigo
						System.exit(0);
						
						break;
					default:
						//Por si nos da un valor que no esta en las opciones
						System.out.println("Opcion invalida");
						break;
					
					}
					//Se termina la ejecucion del do while si la opcion es 4
			}while(opcion != 4);
			
		}catch (Exception e) {
		      System.out.println("Error: " + e);
		      
	    }
	
			
		
		
		
	}
	public void agregarPerro() {
		
		try {
			//Pedimos al ususario todos los datos del perro menos el numero de chip
			
			//Llamamos a la funcion cantAnimales para obtener cuantos animales hay registrados actualmente y le añadimos 1 para este animal
			int num_chip = this.cantAnimales() + 1;
			scan.nextLine();
			
			System.out.println("Nombre del perro");
			String nombre = scan.nextLine();
			
			System.out.println("Edad del perro");
			int edad = scan.nextInt();
			
			scan.nextLine();
			System.out.println("Raza del perro");
			String raza = scan.nextLine();
			
			System.out.println("Adoptado True = Si False = No");
			boolean adoptado = scan.nextBoolean();
			
			scan.nextLine();

			System.out.println("Tamaño del perro Pequeño / Mediano / Grande");
			String size = scan.nextLine();
			
			//Referenciamos el arrayList animales y agregamos una instancia de Perro
			animales.add(new Perro(num_chip, nombre, edad, raza,adoptado,size));
			System.out.println("Perro con numero de chip: " + num_chip + " a sido registrado" );
			
		}catch (Exception e) {
		      System.out.println("Error a la hora de introducir datos intente de nuevo.");
	    }
		
		
	}
	public void agregarGato() {
		try {
			//Pedimos al ususario todos los datos del gato menos el numero de chip

			//Llamamos a la funcion cantAnimales para obtener cuantos animales hay registrados actualmente y le añadimos 1 para este animal

			int num_chip = this.cantAnimales() + 1;
			scan.nextLine();
			
			System.out.println("Nombre");
			String nombre = scan.nextLine();
			
			System.out.println("Edad del gato");
			int edad = scan.nextInt();
			
			scan.nextLine();
			System.out.println("Raza del gato");
			String raza = scan.nextLine();
			
			System.out.println("Adoptado True = Si False = No");
			boolean adoptado = scan.nextBoolean();
			
			System.out.println("Se le ha realizado el test de leucemia True = Si / False = No");
			boolean test = scan.nextBoolean();
			
			//Referenciamos el arrayList animales y agregamos una instancia de Gato
			animales.add(new Gato(num_chip, nombre, edad, raza,adoptado, test));
			System.out.println("Gato con numero de chip: " + num_chip + " a sido registrado" );

		}catch (Exception e) {
		      System.out.println("Error a la hora de introducir datos intente de nuevo.");
	    }
		
		
		
		
	}
	public int cantAnimales() {
		//Metodo que hacemos para comprobar cuantos animales hay en el array para que no de error a la hora de introducir nuevos animales
		int cant  = 0;
		for(Animal animal : animales) {
			
			 cant++;
			
		}
		//Devolvemos la cantidad de estos
		return cant;
		
	}
	public void mostrarAnimales(int num) {
		//Metodo que buscamos un animal que se ha pedido anteriomente y si existe se lo mostramos y si no le decimos que no existe
		for (Animal animal : animales) {
		    if (animal.num_chip == num) {
		        animal.mostrar();
		        return;
		    }
		}
		System.out.println("Animal no encontrado.");
	}
}
