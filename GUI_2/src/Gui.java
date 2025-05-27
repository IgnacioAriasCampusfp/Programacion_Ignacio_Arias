import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Gui {

	
	static String modelo;

    public static void gui() {
        String apiUrl = "https://openrouter.ai/api/v1/chat/completions";

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setLayout(new BorderLayout());
        frame.setTitle("El chato");
        frame.setLocationRelativeTo(null);
        

        String[] modelos = {"qwen/qwen3-32b:free", "mistralai/devstral-small:free","google/gemma-3n-e4b-it:free","meta-llama/llama-3.3-8b-instruct:free"};
        JComboBox<Object> box = new JComboBox<>(modelos);
        box.setSelectedIndex(0);  
        modelo = (String) box.getItemAt(0);
        box.addActionListener(e -> modelo = (String) box.getSelectedItem());

        // Etiqueta de pregunta
        JLabel centerLabel = new JLabel("", SwingConstants.RIGHT);
        centerLabel.setFont(new Font("Arial", Font.BOLD, 15));
        centerLabel.setAlignmentX(Component.RIGHT_ALIGNMENT);
        centerLabel.setBorder(BorderFactory.createEmptyBorder(5, 10, 5, 10)); // margen

        // Área de texto para respuesta
        JTextArea leftLabel = new JTextArea();
        leftLabel.setFont(new Font("Arial", Font.PLAIN, 14));
        leftLabel.setLineWrap(true);
        leftLabel.setWrapStyleWord(true);
        leftLabel.setEditable(false);
        leftLabel.setBackground(null);
        leftLabel.setBorder(BorderFactory.createEmptyBorder(5, 10, 5, 10)); // margen

        JScrollPane scrollRespuesta = new JScrollPane(leftLabel);
        scrollRespuesta.setBorder(null);
        scrollRespuesta.setPreferredSize(new Dimension(450, 300)); // tamaño compacto

        // Panel para mostrar entrada y respuesta
        JPanel displayPanel = new JPanel();
        displayPanel.setLayout(new BoxLayout(displayPanel, BoxLayout.Y_AXIS));
        displayPanel.add(centerLabel);
        displayPanel.add(scrollRespuesta);

        // Panel inferior con campo de texto y botón
        JPanel panel = new JPanel(new FlowLayout());
        JTextField textField = new JTextField(20);
        JButton button = new JButton("Enviar");

        button.addActionListener(e -> {
            String textopregunta = textField.getText();
            centerLabel.setText(textopregunta);

            PeticionOpenRouter.Mensaje[] mensajes = {
                new PeticionOpenRouter.Mensaje("user", textopregunta)
            };

            PeticionOpenRouter peticion = new PeticionOpenRouter(modelo, mensajes);
            String textorespuesta = ClienteApiRest.hacerPost(apiUrl, peticion, RespuestaOpenRouter.class);

            leftLabel.setText(textorespuesta);
        });

        panel.add(textField);
        panel.add(button);

        frame.add(box, BorderLayout.NORTH);
        frame.add(panel, BorderLayout.SOUTH);
        frame.add(displayPanel, BorderLayout.CENTER);

        frame.setVisible(true);
    }

}
