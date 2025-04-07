
public class SensorHumedad extends Sensor implements Medible {

	public SensorHumedad(String id,String ubicacion) {
		this.id = id;
		this.ubicacion = ubicacion;
	}
	
	public double leerValor() {
		return Math.random()*10;
	}

	
	public String getUnidad() {
		return "%";
	}

}
