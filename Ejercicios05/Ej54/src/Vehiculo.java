
public class Vehiculo {
String modelo;
String marca;
public Vehiculo(String modelo, String marca) {
	this.marca = marca;
	this.modelo = modelo;
	
}
public void mostrarDatos() {
	System.out.println(marca + " " + modelo);
}
}
