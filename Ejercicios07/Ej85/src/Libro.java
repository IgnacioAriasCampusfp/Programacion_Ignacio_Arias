
public class Libro extends Item implements Describible {

	String titulo;
	public Libro(String titulo) {
		
		this.titulo = titulo;
	}
	
	public String describir() {
		return "El libro con titulo: " + titulo;
	}

}
