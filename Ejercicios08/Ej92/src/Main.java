import java.io.*;

public class Main {

	public static void main(String[] args) {
		Animal animal = new Animal("Megatron","Gato");
		try {
			ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("animal.ser"));
			out.writeObject(animal);
			out.close();
		}catch (IOException e) {
			e.printStackTrace();
		}
		
		try {
			ObjectInputStream in = new ObjectInputStream(new FileInputStream("animal.ser"));
			Animal animalrecuperado = (Animal) in.readObject();
			in.close();
			System.out.println("Datos recuperados");
			System.out.println("Nombre: " + animalrecuperado.nombre);
			System.out.println("Especie: " + animalrecuperado.especie);

		}  catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

}
