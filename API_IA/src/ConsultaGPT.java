import java.util.Scanner;


public class ConsultaGPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String apiUrl = "https://openrouter.ai/api/v1/chat/completions";
        String modelo = "qwen/qwen3-14b:free"; // modelo gratuito válido

        System.out.println("=== Consulta GPT desde Java (OpenRouter) ===");

        while (true) {
            System.out.print("\nEscribe tu pregunta para el modelo (o escribe 'salir' para terminar): ");
            String pregunta = scanner.nextLine();

            if (pregunta.trim().equalsIgnoreCase("salir")) {
                break;
            }

            // Crear el mensaje
            PeticionOpenRouter.Mensaje[] mensajes = {
                new PeticionOpenRouter.Mensaje("user", pregunta)
            };

            // Crear la petición con el modelo gratuito
            PeticionOpenRouter peticion = new PeticionOpenRouter(modelo, mensajes);

            // Llamar a la API
            ClienteApiRest.hacerPost(apiUrl, peticion, RespuestaOpenRouter.class);
        }

        System.out.println("Programa finalizado.");
        scanner.close();
        
    }
    
    
}
