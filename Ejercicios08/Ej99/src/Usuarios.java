import java.io.Serializable;

public class Usuarios implements Serializable {
String nombre;
String passw;

public Usuarios(String nombre, String passw) {
	
	this.nombre = nombre;
	this.passw = passw;
}
	
}
