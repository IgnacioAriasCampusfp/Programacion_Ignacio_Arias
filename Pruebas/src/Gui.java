import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class Gui{
	
    public static void main(String args[]){

    	MarcoBotones mimarco = new MarcoBotones();
    	mimarco.setVisible(true);
    	mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       

    }
    
    }
class MarcoBotones extends JFrame{
	
	public MarcoBotones() {
		setTitle("");
		setBounds(700,300,500,300);
		LaminaBotones milamina = new LaminaBotones();
		add(milamina);
	}
	
}
class LaminaBotones extends JPanel implements ActionListener{
	JButton botonAzul = new JButton("Azul");
	JButton botonRojo = new JButton("Rojo");

	public LaminaBotones() {
		add(botonAzul);
		add(botonRojo);
		botonAzul.addActionListener(this);
		botonRojo.addActionListener(this);

	}
	public void actionPerformed(ActionEvent e) {
		Object butonPulsado = e.getSource();
		
		if(butonPulsado == botonAzul) {
			setBackground(Color.blue);
		}else if(butonPulsado == botonRojo) {
			setBackground(Color.red);

		}
		
	}
}
