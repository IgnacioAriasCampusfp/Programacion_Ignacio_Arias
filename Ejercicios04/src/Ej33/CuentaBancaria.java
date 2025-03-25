package Ej33;

public class CuentaBancaria {
private double saldo;

	
	public void depositar(double cantidad) {
		this.saldo += cantidad;
	}
	public void retirar(double cantidad) {
		this.saldo -= cantidad;
	}
	public void getSaldo() {
		System.out.println(this.saldo);
		
	}

	
	
	
}