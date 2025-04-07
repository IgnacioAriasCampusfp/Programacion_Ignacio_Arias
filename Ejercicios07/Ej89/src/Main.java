import java.util.HashMap;

public class Main {

	public static void main(String[] args) {
	     HashMap<String, Cuenta> cuentas = new HashMap<>();
	        
	        cuentas.put("1001", new CuentaAhorro("1001", 5000.0, 2.5));
	        cuentas.put("1002", new CuentaCorriente("1002", 2000.0, 1000.0));

	        for (Cuenta cuenta : cuentas.values()) {
	            System.out.println(cuenta.obtenerDetalles());
	        }	}

}
