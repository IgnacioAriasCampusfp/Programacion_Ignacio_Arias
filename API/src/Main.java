import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import com.google.gson.Gson;

class Gato {
    String id;
    String url;
    int width;
    int height;
}

class Chistes {
    String type;
    String setup;
    String punchline;
    int id;
}

public class Main {
    public static void main(String[] args) {
        try {
            String apiUrl = "https://api.thecatapi.com/v1/images/search";
            String apiChistes = "https://official-joke-api.appspot.com/random_joke";

            HttpURLConnection conexion = (HttpURLConnection) new URL(apiUrl).openConnection();
            conexion.setRequestMethod("GET");

            HttpURLConnection conexionChiste = (HttpURLConnection) new URL(apiChistes).openConnection(); // CORREGIDO
            conexionChiste.setRequestMethod("GET");

            BufferedReader reader = new BufferedReader(new InputStreamReader(conexion.getInputStream()));
            StringBuilder respuesta = new StringBuilder();
            String linea;
            while ((linea = reader.readLine()) != null) {
                respuesta.append(linea);
            }
            reader.close();

            BufferedReader readerchiste = new BufferedReader(new InputStreamReader(conexionChiste.getInputStream()));
            StringBuilder respuestachiste = new StringBuilder();
            String lineachiste;
            while ((lineachiste = readerchiste.readLine()) != null) {
                respuestachiste.append(lineachiste); // CORREGIDO
            }
            readerchiste.close();

            Gson gson = new Gson();

            Gato[] gatos = gson.fromJson(respuesta.toString(), Gato[].class);
            Chistes chiste = gson.fromJson(respuestachiste.toString(), Chistes.class);
            String json = gson.toJson(gatos);
            System.out.println(json);


            if (gatos.length > 0) {
                System.out.println("\nID del gato: " + gatos[0].id);
                System.out.println("Imagen de gato:");
                System.out.println(gatos[0].url);
            } else {
                System.out.println("No se encontraron gatos.");
            }

            System.out.println("\nChiste:");
            System.out.println(chiste.setup);
            System.out.println(chiste.punchline);

            conexion.disconnect();
            conexionChiste.disconnect();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
