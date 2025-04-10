
public abstract class BibliotecaEscolar {
	

	protected String codigo;
	protected String titulo;
	protected int anioPublicacion;
	
	public BibliotecaEscolar(String codigo, String titulo, int anioPublicacion) {
		this.codigo = codigo;
		this.titulo = titulo;
		this.anioPublicacion = anioPublicacion;
	}
	
	public String getCodigo() {
       return codigo;
   }

}
