import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class Main {

	public static void main(String[] args) {
        gui();

	}
	public static void gui() {
    	JFrame frame = new JFrame();
    	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    	frame.setSize(500,500);
    	frame.setLayout(new BorderLayout());
    	frame.setVisible(true);
    	
    	String[] modelos = {"chatgpt"};
    	JComboBox box = new JComboBox(modelos);
    	
    	JPanel panel1 = new JPanel();
    	
    	panel1.setBackground(Color.red);
    	
    	panel1.setPreferredSize(new Dimension(100,100));
    
    	frame.add(panel1,BorderLayout.CENTER);
    	frame.add(box,BorderLayout.NORTH);
	}
}
