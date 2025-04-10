public class Revista extends BibliotecaEscolar{
	private int numero;
	private boolean esMensual;;
	
	public Revista(String codigo, String titulo, int anioPublicacion, int numero, boolean esMensual) {
		super(codigo, titulo, anioPublicacion);
		this.numero = numero;
		this.esMensual = esMensual;
	}
}
