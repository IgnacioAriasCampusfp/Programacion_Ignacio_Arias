	
	public abstract class Tarea implements Comparable<Tarea>,Ejecutable {
	
		
		String descripcion;
		int prioridad;
		public Tarea(String descripcion,int prioridad) {
			this.descripcion = descripcion;
			this.prioridad = prioridad;
			
		}
		@Override
		public int compareTo(Tarea dist) {
			return Integer.compare(this.prioridad,dist.prioridad);
			
		}
	}
