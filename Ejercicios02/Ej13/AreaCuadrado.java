public class AreaCuadrado{
public static void main(String[] args){
AreaCuadrado area = new AreaCuadrado();
System.out.println(area.calcularArea(5));

}
public int calcularArea(int lado){
return lado * lado;
}
}