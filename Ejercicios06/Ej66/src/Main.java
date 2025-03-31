
public class Main {

	public static void main(String[] args) {
		CorreoElectronico email = new CorreoElectronico();
		email.enviarNotificacion();
		MensajeTexto msg = new MensajeTexto();
		msg.enviarNotificacion();
		
	}

}
