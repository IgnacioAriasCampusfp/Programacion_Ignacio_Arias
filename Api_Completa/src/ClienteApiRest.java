import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import com.google.gson.Gson;

// Clase plantilla de cliente API REST
public class ClienteApiRest {
    private static final Gson gson = new Gson();
    private static final String API_KEY = "reqres-free-v1";

    /**
     * Método genérico para hacer peticiones POST enviando un objeto Java como JSON.
     * @param apiUrl  URL completa de la API.
     * @param objetoEnviar  Objeto Java que quieres enviar.
     * @param claseRespuesta  Clase Java que representa la respuesta.
     * @param token  Token opcional (puede ser null).
     * @param <T> Tipo del objeto que envías.
     * @param <R> Tipo de la clase que representa la respuesta.
     */
    public static <T, R> void hacerPost(String apiUrl, T objetoEnviar, Class<R> claseRespuesta, String token) {
        try {
            URL url = new URL(apiUrl);
            HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
            conexion.setRequestMethod("POST");
            conexion.setRequestProperty("Content-Type", "application/json; utf-8");
            conexion.setRequestProperty("Accept", "application/json");
            conexion.setRequestProperty("x-api-key", API_KEY); 

            if (token != null) {
                conexion.setRequestProperty("Authorization", "Bearer " + token);
            }
            conexion.setDoOutput(true);

            String jsonInputString = gson.toJson(objetoEnviar);
            try (OutputStreamWriter writer = new OutputStreamWriter(conexion.getOutputStream())) {
                writer.write(jsonInputString);
            }

            manejarRespuesta(conexion, claseRespuesta);

        } catch (Exception e) {
            System.out.println("Error inesperado en POST:");
            e.printStackTrace();
        }
    }

    /**
     * Método genérico para hacer peticiones GET.
     * @param apiUrl  URL completa de la API.
     * @param token  Token opcional (puede ser null).
     */
    public static void hacerGet(String apiUrl, String token) {
        try {
            URL url = new URL(apiUrl);
            HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
            conexion.setRequestMethod("GET");
            conexion.setRequestProperty("Accept", "application/json");
            conexion.setRequestProperty("x-api-key", API_KEY); // API Key añadida

            if (token != null) {
                conexion.setRequestProperty("Authorization", "Bearer " + token);
            }

            manejarRespuesta(conexion, null);

        } catch (Exception e) {
            System.out.println("Error inesperado en GET:");
            e.printStackTrace();
        }
    }

    /**
     * Método para manejar la respuesta de la API, con gestión de errores.
     * @param conexion  Objeto HttpURLConnection abierto.
     * @param claseRespuesta  Clase esperada en la respuesta (puede ser null para GET sin deserialización).
     * @param <R> Clase de respuesta.
     */
    private static <R> void manejarRespuesta(HttpURLConnection conexion, Class<R> claseRespuesta) {
        try {
            int statusCode = conexion.getResponseCode();
            if (statusCode == 200 || statusCode == 201) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(conexion.getInputStream()));
                if (claseRespuesta != null) {
                    R respuesta = gson.fromJson(reader, claseRespuesta);
                    System.out.println("Respuesta procesada:");
                    System.out.println(gson.toJson(respuesta));
                } else {
                    String linea;
                    while ((linea = reader.readLine()) != null) {
                        System.out.println(linea);
                    }
                }
                reader.close();
            } else {
                mostrarError(conexion, statusCode);
            }
            conexion.disconnect();
        } catch (Exception e) {
            System.out.println("Error al manejar respuesta:");
            e.printStackTrace();
        }
    }

    /**
     * Método para mostrar error personalizado según el código.
     */
    private static void mostrarError(HttpURLConnection conexion, int statusCode) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(conexion.getErrorStream()));
            StringBuilder errorRespuesta = new StringBuilder();
            String linea;
            while ((linea = reader.readLine()) != null) {
                errorRespuesta.append(linea);
            }
            reader.close();

            System.out.println("Código de error: " + statusCode);
            System.out.println("Detalles del error:");
            System.out.println(errorRespuesta.toString());

        } catch (Exception e) {
            System.out.println("No se pudo leer el cuerpo del error.");
        }
    }
}
