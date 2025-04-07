
public class CuentaCorriente extends Cuenta implements Auditable {

	
	
	double limiteSobregiro;
	
	 public CuentaCorriente(String cuenta, double saldo, double limiteSobregiro) {
	        super(cuenta, saldo);
	        this.limiteSobregiro = limiteSobregiro;
	    }	
	 @Override
	 public String obtenerDetalles() {
	        return "Cuenta Corriente - Número: " + cuenta + ", Saldo: " + saldo + ", Límite de Sobregiro: " + limiteSobregiro;
	    }

}
