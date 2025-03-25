
package Ej33;


public class Main {

	public static void main(String[] args) {
		
		CuentaBancaria cuenta1 = new CuentaBancaria();
		cuenta1.depositar(150);
		cuenta1.getSaldo();
		cuenta1.retirar(75);
		cuenta1.getSaldo();
		
	}

}
