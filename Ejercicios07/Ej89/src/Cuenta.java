
public abstract class Cuenta implements Auditable{

	String cuenta;
	double saldo;
	public Cuenta(String cuenta, double saldo) {
        this.cuenta = cuenta;
        this.saldo = saldo;
    }
	
}
