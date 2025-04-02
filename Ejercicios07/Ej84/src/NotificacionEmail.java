
public class NotificacionEmail implements Notificable {

	String direccionCorreo;
	public NotificacionEmail(String direccionCorreo) {
		this.direccionCorreo = direccionCorreo;
	}
	
	public void enviar(String mensaje) {

		System.out.println("Direccion de correo: "  + direccionCorreo + " Mensaje: " + mensaje);
	}

}
