
public class NotificacionSMS implements Notificable {

	String numeroTelefono;
	
	public NotificacionSMS(String numeroTelefono) {
		this.numeroTelefono =  numeroTelefono;
	}
	
	public void enviar(String mensaje) {
		System.out.println("Nº telfono: " + numeroTelefono + " Mensaje: " + mensaje);
	}

}
