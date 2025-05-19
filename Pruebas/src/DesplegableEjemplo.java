import javax.swing.*;

public class DesplegableEjemplo {
    public static void main(String[] args) {
        // Crear la ventana
        JFrame frame = new JFrame("Ejemplo de Desplegable");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Crear el array de opciones
        String[] opciones = { "Opción 1", "Opción 2", "Opción 3" };

        // Crear el JComboBox con las opciones
        JComboBox<String> comboBox = new JComboBox<>(opciones);

        // Agregar una acción al seleccionar un elemento
        comboBox.addActionListener(e -> {
            String seleccion = (String) comboBox.getSelectedItem();
            System.out.println("Seleccionaste: " + seleccion);
        });

        // Añadir el comboBox al frame
        frame.getContentPane().add(comboBox); // por defecto al centro

        // Mostrar la ventana
        frame.setVisible(true);
    }
}
