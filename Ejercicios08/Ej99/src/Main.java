import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
	static Scanner scanner = new Scanner(System.in);
	static ArrayList<Usuarios> usuarios = new ArrayList<Usuarios>();
	public static void main(String[] args) {
		Main mn = new Main();
		mn.menu();
		
	}
	
	public void menu() {
		int opcion;

        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Añadir nuevo usuario");
            System.out.println("2. Validar usuario");
            System.out.println("0. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); 

            switch (opcion) {
                case 1:
                	aniadirUsuario();
                	break;
                case 2:
                	System.out.println("Introduze el nombre de usuario: ");
                	String nombre = scanner.nextLine();
                	System.out.println("Introduze la contraseña: ");
                	String passw = scanner.nextLine();
                	validarUsuario(nombre,passw);
                	break;
                case 0:
                    System.out.println("Saliendo del programa.");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 0);
    }
	public static void aniadirUsuario() {
		try {
            System.out.print("Nombre: ");
            String nombre = scanner.nextLine();
            System.out.print("Contraseña: ");
            String passw = scanner.nextLine();

            usuarios.add(new Usuarios(nombre, passw));
           
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("usuarios.ser"));
            out.writeObject(usuarios);
            out.close();

            System.out.println("Producto añadido correctamente.");
            
            
        } catch (InputMismatchException e) {
            System.out.println("Error: Entrada no válida. Inténtalo de nuevo.");
            scanner.nextLine();
        } catch (IOException  e) {
            System.out.println("Error al guardar el usuario: " + e.getMessage());
        }
	}
	
@SuppressWarnings("unchecked")
public static void validarUsuario(String user, String passw) {
		boolean registrado = false;
		try {
			
        	ObjectInputStream in = new ObjectInputStream(new FileInputStream("usuarios.ser"));
			ArrayList<Usuarios> usuarios_rec = (ArrayList<Usuarios>) in.readObject();
            in.close();
            for(Usuarios usr : usuarios_rec) {
            	if(usr.nombre.equals(user) && usr.passw.equals(passw)) {
            		System.out.println("Registro completo");
            		registrado = true;
            		break;
            	}
            	
            }
            if(registrado != true) {
            	System.out.println("Credenciales incorrectas");
            }
            

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error al leer usuarios: " + e.getMessage());
        }

	}


}
