import java.util.Scanner;


public class PruebaApi {
	static Scanner scan = new Scanner(System.in);
    static  String urlPost = "https://reqres.in/api/users";
    static String token = "1234567890abcdef"; // Token ficticio (puede ser null si no es necesaria autenticación)
    static String urlGet = "https://reqres.in/api/users?page=2";

    public static void main(String[] args) {


        PruebaApi.menu();
        



    }
    public static void menu() {
    	
    	int opcion = 0;
    	do {
			System.out.print("Menu\n1 - Agregar usuario \n2 - Obtener usuarios\n3 - Agregar productos \n Elige una opcion:");
	        opcion = scan.nextInt();

    		switch(opcion){
    		case 1:
    			scan.nextLine();
    	        System.out.print("Nombre: ");
    	        String nombre = scan.nextLine();
    	        System.out.print("Cargo: ");
    	        String cargo = scan.nextLine();
    	        
    	        if(nombre == "" || cargo == "" || nombre == "" && cargo == "") {
    	        	System.out.println("Los valores son nulos");
    	        }else {
    	        	Usuario usuario = new Usuario(nombre,cargo);
        	        ClienteApiRest.hacerPost(urlPost, usuario, UsuarioRespuesta.class, token);

    	        }
    	        break;
    		case 2:
    	        ClienteApiRest.hacerGet(urlGet, token);
    			break;
    		case 3:
    			scan.nextLine();
    	        System.out.print("Nombre producto: ");
    	        String nombrep = scan.nextLine();
    	        System.out.print("Precio: ");
    	        double precio = scan.nextDouble();
    	        System.out.println(precio);
    	        if(nombrep == "" || precio == 0 || nombrep == "" && precio == 0) {
    	        	System.out.println("Los valores son nulos");
    	        }else {
    	        	Producto producto = new Producto(nombrep,precio);
        	        ClienteApiRest.hacerPost(urlPost, producto, ProductoRespuesta.class, token);

    	        }
    	        
    	        
    			
    			break;
    		default:
    			
    			break;
    		}
    	}while(opcion != 0);
    	
    	
    	
    }
}
