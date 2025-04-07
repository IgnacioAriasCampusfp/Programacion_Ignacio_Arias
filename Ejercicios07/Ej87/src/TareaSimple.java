
public class TareaSimple extends Tarea implements Ejecutable {

	public TareaSimple(String descripcion,int prioridad) {
		super(descripcion,prioridad);
	}
	@Override
	public void ejecutar() {
		System.out.println("Ejecutando tarea simple: " + descripcion);
	}
}
