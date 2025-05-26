import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class Main extends JFrame{

	public static void main(String[] args) {
        gui();

	}
	public static void gui() {
	    JFrame frame = new JFrame();
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setSize(500, 500);
	    frame.setLayout(new BorderLayout());

	    String[] modelos = {"chatgpt", "deepseek"};
	    JComboBox<Object> box = new JComboBox<Object>(modelos);

	    // Etiquetas para mostrar los textos en distintas filas
	    JLabel leftLabel = new JLabel("", SwingConstants.LEFT);
	    leftLabel.setFont(new Font("Arial", Font.BOLD, 15));
	    leftLabel.setVerticalAlignment(SwingConstants.CENTER);

	    JLabel centerLabel = new JLabel("", SwingConstants.RIGHT);
	    centerLabel.setFont(new Font("Arial", Font.BOLD, 15));
	    centerLabel.setVerticalAlignment(SwingConstants.CENTER);

	    // Panel para mostrar los labels en distintas filas
	    JPanel displayPanel = new JPanel(new GridLayout(2, 1)); // 2 filas, 1 columna
	    displayPanel.add(centerLabel);   // primera fila
	    displayPanel.add(leftLabel); // segunda fila

	    // Panel inferior con el campo de texto y botón
	    JPanel panel = new JPanel(new FlowLayout());
	    JTextField textField = new JTextField(20);
	    JButton button = new JButton("Enviar");

	    button.addActionListener(new ActionListener() {
	        @Override
	        public void actionPerformed(ActionEvent e) {
	            String textopregunta = textField.getText();
	            centerLabel.setText(textopregunta);

	            String textorespuesta = "¡Caramba!";
	            leftLabel.setText(textorespuesta);
	        }
	    });

	    panel.add(textField);
	    panel.add(button);

	    // Agregar componentes al frame
	    frame.add(box, BorderLayout.NORTH);
	    frame.add(panel, BorderLayout.SOUTH);
	    frame.add(displayPanel, BorderLayout.CENTER); 

	    frame.setVisible(true);
	}
}
