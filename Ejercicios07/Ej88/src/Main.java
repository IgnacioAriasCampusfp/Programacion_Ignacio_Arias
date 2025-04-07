import java.util.*;

public class Main {

	public static void main(String[] args) {

		
		ArrayList<Sensor> sensores = new ArrayList<>();
		sensores.add(new SensorTemperatura("1","Carabanchel"));
		sensores.add(new SensorHumedad("1","Carabanchel"));
		sensores.add(new SensorTemperatura("2","Ciudad Real"));
		sensores.add(new SensorHumedad("2","Ciudad Real"));
		sensores.add(new SensorTemperatura("3","Logroño"));
		sensores.add(new SensorHumedad("3","Logroño"));
		
		HashMap<String,Double> lecturas = new HashMap<>();
		
		for(Sensor sensor : sensores) {
				
			lecturas.put(sensor.id, sensor.leerValor());
			System.out.println("Sensor: " + sensor.id + " en " + sensor.ubicacion + ": " + " " + sensor.leerValor() + " " +sensor.getUnidad());

		}
		

	}

}
