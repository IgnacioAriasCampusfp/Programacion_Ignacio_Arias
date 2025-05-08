package CRUD;

import java.sql.*;
import java.sql.Date;
import java.util.*;

public class Menu {
	static Scanner scanner = new Scanner(System.in);
	static ClienteController controlador_cli = new ClienteController();
	static ProveedoresController controlador_pro = new ProveedoresController();
	static ArticulosController controlador_ar = new ArticulosController();
	static FacturaController controlador_fac = new FacturaController();
	static VentasController controlador_ven = new VentasController();


	
	public  void menuPrincipal() {
	       int opcion = 0;

	        do {
	        	try {	
	        	//Imprimimos el menu.
	            System.out.println("----- MENÚ ----- \n 1 – Gestión de Clientes \n 2 - Gestión de Proveedores "
	            		+ "\n 3 - Gestión de Artículos \n 4 - Gestión de Facturas Recibidas \n 5 – Gestión de Ventas \n 6 - Informes de Ventas por Cliente \n 7 - Salir");
	            System.out.print("Elige una opción: ");
	            //Le pedimos al usuario que no de una opcion.
	            opcion = scanner.nextInt();

	            switch (opcion) {
	            //Si el usuario no da la opcion 1 llamaremos a verPeliculas del Controlador
	            case 1:
	            	this.menuCliente();
	            	break;                 
	            case 2:      
	            	this.menuProveedores();
	                break;
	            case 3:
	            	this.menuArticulos();
	                 break;
	            case 4:                 
	            	this.menuFacturas();
	                 break;
	            case 5:
	            	this.menuVentas();
	            	break;
	            case 6:
	            	 System.out.print("ID del cliente: ");
	                    int idInforme = scanner.nextInt();
	                    controlador_cli.informePorCliente(idInforme);
	                    break;
	
	            case 7:
	                 System.out.println("Terminando programa.");              
	                 break;
		         }

	            System.out.println();
	            //Si da error nos saldrá un aviso del programa
	        	}catch(Exception e) {
	        	    System.out.println("Error: " + e.getMessage());
	        	    scanner.nextLine(); 
	        	}
	        	//Terminaremos el bucle si la opcion elegida es 2
	        } while (opcion != 7);

	        scanner.close();
	    }
	public void menuCliente() {
		int opcion;

        do {
            System.out.println("\n--- MENÚ ---");
            System.out.println("1. Crear Cliente");
            System.out.println("2. Listar Clientes");
            System.out.println("3. Modificar Cliente");
            System.out.println("4. Eliminar Cliente");
            System.out.println("5. Ver Informe por Cliente");
            System.out.println("0. Salir");
            System.out.print("Opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1:
                    System.out.print("Nombre: ");
                    String nombre = scanner.nextLine();
                    System.out.print("Email: ");
                    String email = scanner.nextLine();
                    System.out.print("Teléfono: ");
                    String telefono = scanner.nextLine();
                    controlador_cli.anadirCliente(nombre, email, telefono);
                    break;
                case 2:
                	controlador_cli.listarClientes();
                    break;
                case 3:
                    System.out.print("ID del cliente a modificar: ");
                    int id = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nuevo nombre: ");
                    nombre = scanner.nextLine();
                    System.out.print("Nuevo email: ");
                    email = scanner.nextLine();
                    System.out.print("Nuevo teléfono: ");
                    telefono = scanner.nextLine();
                    controlador_cli.actualizarCliente(id, nombre, email, telefono);
                    break;
                case 4:
                    System.out.print("ID del cliente a eliminar: ");
                    int idEliminar = scanner.nextInt();
                    controlador_cli.eliminarCliente(idEliminar);
                    break;
             
            }
        } while (opcion != 0);

        scanner.close();
    }

	
	public void menuProveedores() {
        int op;
        do {
            System.out.println("\n-- Gestión de Proveedores --");
            System.out.println("1. Crear Proveedores");
            System.out.println("2. Listar Proveedores");
            System.out.println("3. Modificar Proveedores");
            System.out.println("4. Eliminar Proveedores");
            System.out.println("0. Volver");
            op = scanner.nextInt(); scanner.nextLine();

            switch (op) {
                case 1 -> {
                    System.out.print("Nombre: "); String n = scanner.nextLine();
                    System.out.print("CIF: "); String cif = scanner.nextLine();
                    System.out.print("Teléfono: "); String t = scanner.nextLine();
                    controlador_pro.crearProveedor(n, cif, t);
                }
                case 2 -> controlador_pro.listarProveedores();
                case 3 -> {
                    System.out.print("ID: "); int id = scanner.nextInt(); scanner.nextLine();
                    System.out.print("Nuevo nombre: "); String n = scanner.nextLine();
                    System.out.print("Nuevo CIF: "); String cif = scanner.nextLine();
                    System.out.print("Nuevo teléfono: "); String t = scanner.nextLine();
                    controlador_pro.modificarProveedor(id, n, cif, t);
                }
                case 4 -> {
                    System.out.print("ID: "); int id = scanner.nextInt();
                    controlador_pro.eliminarProveedor(id);
                }
            }
        } while (op != 0);
    }
	public  void menuArticulos() {
        int op;
        do {
            System.out.println("\n-- Gestión de Artículos --");
            System.out.println("1. Crear Articulo");
            System.out.println("2. Listar Articulos");
            System.out.println("3. Modificar Articulos");
            System.out.println("4. Eliminar Articulos");
            System.out.println("0. Volver");
            op = scanner.nextInt(); scanner.nextLine();

            switch (op) {
                case 1 -> {
                    System.out.print("Nombre: "); String n = scanner.nextLine();
                    System.out.print("Precio: "); double p = scanner.nextDouble();
                    System.out.print("Stock: "); int s = scanner.nextInt();
                    controlador_ar.crearArticulo(n, p, s);
                }
                case 2 -> controlador_ar.listarArticulos();
                case 3 -> {
                    System.out.print("ID: "); int id = scanner.nextInt(); scanner.nextLine();
                    System.out.print("Nuevo nombre: "); String n = scanner.nextLine();
                    System.out.print("Nuevo precio: "); double p = scanner.nextDouble();
                    System.out.print("Nuevo stock: "); int s = scanner.nextInt();
                    controlador_ar.modificarArticulo(id, n, p, s);
                }
                case 4 -> {
                    System.out.print("ID: "); int id = scanner.nextInt();
                    controlador_ar.eliminarArticulo(id);
                }
            }
        } while (op != 0);
    }
	public void menuFacturas() {
        int op;
        do {
            System.out.println("\n-- Gestión de Facturas Recibidas --");
            System.out.println("1. Crear Factura");
            System.out.println("2. Listar Facturas");
            System.out.println("3. Modificar Factura");
            System.out.println("4. Eliminar Factura");
            System.out.println("0. Volver");
            op = scanner.nextInt(); scanner.nextLine();

            switch (op) {
                case 1 -> {
                    System.out.print("ID Proveedor: "); int idProv = scanner.nextInt();
                    System.out.print("Fecha (AAAA-MM-DD): "); String f = scanner.next(); scanner.nextLine();
                    System.out.print("Total: "); double t = scanner.nextDouble();
                    controlador_fac.crearFactura(idProv, Date.valueOf(f), t);
                }
                case 2 -> controlador_fac.listarFacturas();
                case 3 -> {
                    System.out.print("ID Factura: "); int id = scanner.nextInt();
                    System.out.print("ID Proveedor: "); int idProv = scanner.nextInt();
                    System.out.print("Fecha (AAAA-MM-DD): "); String f = scanner.next();
                    System.out.print("Total: "); double t = scanner.nextDouble();
                    controlador_fac.modificarFactura(id, idProv, Date.valueOf(f), t);
                }
                case 4 -> {
                    System.out.print("ID Factura: "); int id = scanner.nextInt();
                    controlador_fac.eliminarFactura(id);
                }
            }
        } while (op != 0);
    }
	public void menuVentas() {
        int op;
        do {
            System.out.println("\n-- Gestión de Ventas --");
            System.out.println("1. Registrar venta");
            System.out.println("2. Listar ventas");
            System.out.println("3. Modificar venta");
            System.out.println("4. Eliminar venta");
            System.out.println("0. Volver");
            op = scanner.nextInt(); scanner.nextLine();

            switch (op) {
                case 1 -> {
                    System.out.print("ID Cliente: "); int idCli = scanner.nextInt();
                    System.out.print("ID Artículo: "); int idArt = scanner.nextInt();
                    System.out.print("Cantidad: "); int cant = scanner.nextInt();
                    System.out.print("Fecha (AAAA-MM-DD): "); String f = scanner.next(); scanner.nextLine();
                    controlador_ven.registrarVenta(idCli, idArt, cant, Date.valueOf(f));
                }
                case 2 -> controlador_ven.listarVentas();
                case 3 -> {
                    System.out.print("ID Venta: "); int id = scanner.nextInt();
                    System.out.print("ID Cliente: "); int idCli = scanner.nextInt();
                    System.out.print("ID Artículo: "); int idArt = scanner.nextInt();
                    System.out.print("Cantidad: "); int cant = scanner.nextInt();
                    System.out.print("Fecha (AAAA-MM-DD): "); String f = scanner.next();
                    controlador_ven.modificarVenta(id, idCli, idArt, cant, Date.valueOf(f));
                }
                case 4 -> {
                    System.out.print("ID Venta: "); int id = scanner.nextInt();
                    controlador_ven.eliminarVenta(id);
                }
            }
        } while (op != 0);
    }
}


