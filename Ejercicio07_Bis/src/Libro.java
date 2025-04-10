public class Libro extends BibliotecaEscolar{
	private String autor;
	private int paginas;
	
	public Libro(String codigo, String titulo, int anioPublicacion, String autor, int paginas) {
		super(codigo, titulo, anioPublicacion);
		this.autor = autor;
		this.paginas = paginas;
	}
}
