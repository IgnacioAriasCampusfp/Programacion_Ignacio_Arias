package Hito;

//Importar java.util para el uso de arraylist y scanner
import java.util.*;
	public class Programación_H1_Parte_1_3doT_IgnacioArias {
		//Creamos instancia de scanner y de el arrayList de animal
		Scanner scan = new Scanner(System.in);	
		static ArrayList<Animal> animales = new ArrayList<>();
		ArrayList<Persona> persona = new ArrayList<>();

		
		
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
					System.out.println("1 - Dar de alta 2 - Listar animales 3 - Buscar animal 4 - Realizar adopcion 5 - Dar de baja 6 - Estadisticas gatos 7 - Salir");
					opcion = scan.nextInt();
						switch (opcion) {
						case 1:
							//Llamamos a menuAnimales para registrar que animal
							this.menuAnimales();
							break;
							
						case 2:
							//Llamamos a mostrarAnimales para mostrar todos los animales
							this.mostrarAnimales();
							break;
						case 3:
							//llamamos a buscarAnimal con un paso antes que es pedirle el numero de chip del animal buscado
	
							System.out.println("Numero del animal buscado");
							int num = scan.nextInt();
							this.buscarAnimales(num);
							break;
						case 4:
							System.out.println("Que animal desea adoptar: ");
							int chip = scan.nextInt();
							this.realizarAdopcion(chip);
							break;
						case 5:
						    System.out.println("Ingrese el número de chip del animal a eliminar:");
						    int chipBaja = scan.nextInt();
						    this.darDeBaja(chipBaja);
						    break;
						case 6:
							System.out.println("Gatos registrados: " + this.contarGatos() + " ,gatos que tienen el test de leucemia: " + 	this.contarGatosTest());
							break;
							
						case 7:
						    System.exit(0);
						    break;
	
						default:
							//Por si nos da un valor que no esta en las opciones
							System.out.println("Opcion invalida");
							break;
						
						}
						//Se termina la ejecucion del do while si la opcion es 7
				}while(opcion != 7);
				
			}catch (Exception e) {
			      System.out.println("Error: " + e);
			      
		    }
		
				
			
			
			
		}
	public void menuAnimales() {
		try {
			int opcion;
	
			System.out.println("Que desea hacer: 1 - Dar de alta Perro 2 - Dar de alta Gato");
			opcion = scan.nextInt();
	
			switch(opcion) {
			case 1:
				//llamamos a agregarPerro si la opcion elegida es 1
				this.agregarPerro();
				break;
			case 2:
				//llamamos a agregarGato si la opcion elegida es 2
				this.agregarGato();
				break;
			}
			
		}catch(Exception e) {
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
	public void buscarAnimales(int num) {
			//Metodo que buscamos un animal que se ha pedido anteriomente y si existe se lo mostramos y si no le decimos que no existe
			for (Animal animal : animales) {
			    if (animal.num_chip == num) {
			        animal.mostrar();
			        return;
			    }
			}
			System.out.println("Animal no encontrado.");
	}
	
	public void darDeBaja(int num_chip) {
	    try {
	        boolean animalEliminado = false;

	        // Buscar y eliminar el animal
	        Iterator<Animal> iterador = animales.iterator();
	        while (iterador.hasNext()) {
	            Animal animal = iterador.next();
	            if (animal.num_chip == num_chip) {
	                iterador.remove();
	                animalEliminado = true;
	                System.out.println("El animal con el número de chip " + num_chip + " ha sido eliminado.");
	                break;
	            }
	        }

	        if (animalEliminado == false) {
	            System.out.println("Animal no encontrado.");
	            return;
	        }

	        // Actualizamos los chip de los adoptantes si es necesario
	        for(Persona per : persona) {
	            for (Animal animal : animales) {
	                if (per.num_chip_adoptado == animal.num_chip) {
	                    per.num_chip_adoptado = per.num_chip_adoptado - 1;  // Ajustamos el número de chip del adoptante
	                }
	            }
	        }

	        // Reorganizamos los num_chip para que no haya huecos
	        int nuevoChip = 1;
	        for (Animal animal : animales) {
	            animal.num_chip = nuevoChip;  // Reasignamos el número de chip
	            nuevoChip++;
	        }
	        
	    } catch (Exception e) {
	        System.out.println("Error: " + e);
	    }
	}

		    
		
		
		
	public int contarGatos() {
		//Metodo para contar cuantos gatos hay
		    int cantidadGatos = 0;
		    for (Animal animal : animales) {
		        if (animal instanceof Gato) {
		            cantidadGatos++;
		        }
		    }
		    return cantidadGatos;
		}
	public int contarGatosTest() {
		//Metodo para contar cuantos gatos con el test realizado hay

		    int gatos_test = 0;
		    for (Animal animal : animales) {
		        if (animal instanceof Gato && ((Gato) animal).test_leucemia == true) {
		        	gatos_test++;
		        }
		        
		    }
		    return gatos_test;
		}
	
	public void mostrarAnimales() {
		//metodo para mostrar todos los animales sin adoptar
			for(Animal animal : animales) {
				//Si esta adoptado no muestra nada, si lo está muestra sus datos
				if(animal.adoptado) {
					
				}else {
					animal.mostrar();
				}
			}
			
		}
	public void realizarAdopcion(int num_chip) {
	    try {
	        boolean encontrado = false;
	        for (Animal animal : animales) {
	            if (animal.num_chip == num_chip) {
	                encontrado = true;
	                if (animal.adoptado) {
	                    System.out.println("Este animal ya está adoptado.");
	                } else {
	                    // Pedir datos del adoptante
	                    scan.nextLine();
	                    System.out.println("Introduzca el nombre del adoptante: ");
	                    String nombre = scan.nextLine();
	                    System.out.println("Introduzca el DNI:");
	                    String dni = scan.nextLine();

	                    // añadimos a la persona que adopta 
	                    persona.add(new Persona(nombre, dni, num_chip));

	                    // Marcamos el animal como adoptado
	                    animal.adoptado = true;
	                    System.out.println("Adopción realizada exitosamente para el animal con chip: " + num_chip);
	                }
	                break;
	            }
	        }
	        if (!encontrado) {
	            System.out.println("Animal no encontrado.");
	        }
	    } catch (Exception e) {
	        System.out.println("Error: " + e);
	    }
	}
}