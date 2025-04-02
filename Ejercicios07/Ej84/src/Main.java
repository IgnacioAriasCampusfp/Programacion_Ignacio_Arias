import java.util.LinkedList;

public class Main {

	public static void main(String[] args) {

		LinkedList<Notificable> notis = new LinkedList<>();
		notis.add(new NotificacionEmail("asfn@gmail.com"));
		notis.add(new NotificacionEmail("nio234@gmail.com"));
		notis.add(new NotificacionEmail("dsfan123124@gmail.com"));
		notis.add(new NotificacionEmail("soraaaaaaaaa@gmail.com"));
		notis.add(new NotificacionSMS("65212348"));
		notis.add(new NotificacionSMS("68451602"));
		notis.add(new NotificacionSMS("67462114"));
		notis.add(new NotificacionSMS("69875641"));

		for(Notificable noti : notis) {
			
			noti.enviar("Mensaje de SPAM");
		}

	}

}
