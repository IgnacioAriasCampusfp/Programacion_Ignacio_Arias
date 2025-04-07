
public class SensorTemperatura extends Sensor implements Medible {

	
	public SensorTemperatura(String id,String ubicacion) {
		this.id = id;
		this.ubicacion = ubicacion;
		
	}
	
	
	public double leerValor() {
		return Math.random()*10;
	}

	
	public String getUnidad() {
		return "ºC";
	}

}
