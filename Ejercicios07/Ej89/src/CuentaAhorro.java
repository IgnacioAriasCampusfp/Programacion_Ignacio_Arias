
public class CuentaAhorro extends Cuenta implements Auditable {

	double tasaIntereses;
	
	 public CuentaAhorro(String cuenta, double saldo, double tasaIntereses) {
	        super(cuenta, saldo);
	        this.tasaIntereses = tasaIntereses;
	    }
	
	public String obtenerDetalles() {
		return "Cuenta: " + cuenta + " con saldo: " + saldo + " con un interes de: " + tasaIntereses;
	}

}
