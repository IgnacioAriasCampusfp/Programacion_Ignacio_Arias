import java.util.Scanner;


public class PruebaApi {
    public static void main(String[] args) {
    	Scanner scan = new Scanner(System.in);

        String urlPost = "https://reqres.in/api/users";
        String token = "1234567890abcdef"; // Token ficticio (puede ser null si no es necesaria autenticación)

        System.out.print("Nombre: ");
        String nombre = scan.nextLine();
        System.out.print("Cargo: ");
        String cargo = scan.nextLine();
        Usuario usuario = new Usuario(nombre,cargo);
        ClienteApiRest.hacerPost(urlPost, usuario, UsuarioRespuesta.class, token);


        String urlGet = "https://reqres.in/api/users?page=2";
        ClienteApiRest.hacerGet(urlGet, token);
    }
}
