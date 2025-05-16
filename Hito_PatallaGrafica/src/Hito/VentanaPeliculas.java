package Hito;


import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;

public class VentanaPeliculas extends JFrame {
    Controlador_Peliculas controlador = new Controlador_Peliculas();
    

    public VentanaPeliculas() {
        setTitle("Gestión de Películas");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Crear botones
        JButton verBtnPantalla = new  JButton("Ver Peliculas");
        JButton agregarBtn = new JButton("Añadir Película");
        JButton editarBtn = new JButton("Editar Película");
        JButton eliminarBtn = new JButton("Eliminar Película");
        

        // Añadir listeners a los botones
        
        //Ver peliculas listener
        
        verBtnPantalla.addActionListener(e -> {
            ResultSet rs = controlador.verPeliculas();
            
            // Encabezados de la tabla
            String[] columnNames = {"ID", "Título", "Valoraciones", "Categoría", "Fecha de Lanzamiento"};
            
            // Lista para almacenar las filas
            java.util.List<String[]> dataList = new java.util.ArrayList<>();
            
            try {
                while (rs.next()) {

                    String id = rs.getString("id_pelicula");
                    String titulo = rs.getString("Titulo");
                    String valoraciones = rs.getString("Valoraciones");
                    String categoria = rs.getString("Catg");
                    String fecha = rs.getString("Lanzamiento");

                    // Añadir fila a la lista
                    dataList.add(new String[] {id, titulo, valoraciones, categoria, fecha});
                }

                // Convertir la lista a un arreglo 2D
                String[][] data = new String[dataList.size()][];
                data = dataList.toArray(data);

                // Crear tabla
                JTable table = new JTable(data, columnNames);
                JScrollPane scrollPane = new JScrollPane(table);
                table.setFillsViewportHeight(true);

                // Mostrar tabla en un JOptionPane
                JOptionPane.showMessageDialog(null, scrollPane, "Películas", JOptionPane.INFORMATION_MESSAGE);
                
            } catch (SQLException e1) {
                e1.printStackTrace();
                JOptionPane.showMessageDialog(null, "Error al obtener los datos.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
        
        

        
        agregarBtn.addActionListener(e -> {
        	controlador.verCategoria();
            JTextField tituloField = new JTextField();
            JTextField valoracionesField = new JTextField();
            JTextField idCategoriaField = new JTextField();
            JTextField lanzamientoField = new JTextField();

            Object[] campos = {
                "Título:", tituloField,
                "Valoraciones:", valoracionesField,
                "ID Categoría:", idCategoriaField,
                "Lanzamiento (YYYY-MM-DD):", lanzamientoField
            };

            int result = JOptionPane.showConfirmDialog(null, campos, "Nueva Película", JOptionPane.OK_CANCEL_OPTION);
            if (result == JOptionPane.OK_OPTION) {
                String titulo = tituloField.getText();
                String valoraciones = valoracionesField.getText();
                int idCategoria = Integer.parseInt(idCategoriaField.getText());
                Date lanzamiento = Date.valueOf(lanzamientoField.getText());
                controlador.anadirPelicula(titulo, valoraciones, idCategoria, lanzamiento);
            }
        });

        editarBtn.addActionListener(e -> {
            JTextField idField = new JTextField();
            JTextField tituloField = new JTextField();
            JTextField valoracionesField = new JTextField();
            JTextField idCategoriaField = new JTextField();
            JTextField lanzamientoField = new JTextField();
            controlador.verPeliculas();
        	controlador.verCategoria();

            Object[] campos = {
                "ID Película a editar:", idField,
                "Nuevo Título:", tituloField,
                "Nuevas Valoraciones:", valoracionesField,
                "Nuevo ID Categoría:", idCategoriaField,
                "Nuevo Lanzamiento (YYYY-MM-DD):", lanzamientoField
            };

            int result = JOptionPane.showConfirmDialog(null, campos, "Editar Película", JOptionPane.OK_CANCEL_OPTION);
            if (result == JOptionPane.OK_OPTION) {
                int id = Integer.parseInt(idField.getText());
                String titulo = tituloField.getText();
                String valoraciones = valoracionesField.getText();
                int idCategoria = Integer.parseInt(idCategoriaField.getText());
                Date lanzamiento = Date.valueOf(lanzamientoField.getText());
                controlador.editarPelicula(id, titulo, valoraciones, idCategoria, lanzamiento);
            }
        });

        eliminarBtn.addActionListener(e -> {
        	controlador.verPeliculas();
            String idStr = JOptionPane.showInputDialog("Introduce el ID de la película a eliminar:");
            if (idStr != null) {
                int id = Integer.parseInt(idStr);
                controlador.eliminarPelicula(id);
            }
        });
        

        // Panel para los botones
        JPanel panel = new JPanel(new GridLayout(4, 1, 10, 10));
        eliminarBtn.setBackground(Color.red);
        eliminarBtn.setForeground(Color.black);
        panel.add(verBtnPantalla);
        panel.add(agregarBtn);
        panel.add(editarBtn);
        panel.add(eliminarBtn);
        

        add(panel, BorderLayout.CENTER);
    }

    }
