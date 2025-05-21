import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class ClienteApiRest {
    private static final Gson gson = new GsonBuilder().setPrettyPrinting().create();
    static String apiKey = "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";


    public static <T, R> void hacerPost(String apiUrl, T objetoEnviar, Class<R> claseRespuesta) {
        try {
            URL url = new URL(apiUrl);
            HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
            conexion.setRequestMethod("POST");
            conexion.setRequestProperty("Content-Type", "application/json; utf-8");
            conexion.setRequestProperty("Accept", "application/json");
            conexion.setRequestProperty("Authorization", "Bearer " + apiKey);
            conexion.setRequestProperty("HTTP-Referer", "https://tusitio.com");
            conexion.setRequestProperty("X-Title", "MiAplicacionGPT");
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

    private static <R> void manejarRespuesta(HttpURLConnection conexion, Class<R> claseRespuesta) {
        try {
            int statusCode = conexion.getResponseCode();
            BufferedReader reader = new BufferedReader(new InputStreamReader(
                    (statusCode >= 200 && statusCode < 300)
                        ? conexion.getInputStream()
                        : conexion.getErrorStream()
            ));

            StringBuilder respuestaRaw = new StringBuilder();
            String linea;
            while ((linea = reader.readLine()) != null) {
                respuestaRaw.append(linea);
            }
            reader.close();

            if (statusCode == 200 || statusCode == 201) {
                if (claseRespuesta != null) {
                    R respuesta = gson.fromJson(respuestaRaw.toString(), claseRespuesta);
                    if (respuesta instanceof RespuestaOpenRouter) {
                        RespuestaOpenRouter res = (RespuestaOpenRouter) respuesta;
                        if (res.choices != null && res.choices.length > 0) {
                            System.out.println("Respuesta de GPT: " + res.choices[0].message.content);
                        } else {
                            System.out.println("Respuesta sin contenido útil:");
                            System.out.println(gson.toJson(res));
                        }
                    } else {
                        System.out.println(gson.toJson(respuesta));
                    }
                }
            } else {
                System.out.println("Código de error HTTP: " + statusCode);
                System.out.println("Respuesta del servidor:");
                System.out.println(respuestaRaw.toString());
            }

            conexion.disconnect();

        } catch (Exception e) {
            System.out.println("Error al manejar respuesta:");
            e.printStackTrace();
        }
    }
}

