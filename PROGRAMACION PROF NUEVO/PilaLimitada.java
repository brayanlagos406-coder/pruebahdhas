import java.util.Scanner;

class Nodo {
    Object contenido;
    Nodo siguiente;

    Nodo(Object contenido) {
        this.contenido = contenido;
    }
}

public class PilaLimitada {
    Nodo primeroDeLaPila;
    int capacidadMaxima;
    int cantidadActual;

    public PilaLimitada(int max) {
        this.capacidadMaxima = max;
        this.cantidadActual = 0;
    }

    // Apilar (Push) con límite
    public void apilar(Object nuevoObjeto) {
        if (cantidadActual >= capacidadMaxima) {
            System.out.println("ERROR: cartucho lleno (" + capacidadMaxima
                    + " baterías). ¡El cañón explotaría!");
            return;
        }
        Nodo nuevoNodo = new Nodo(nuevoObjeto);
        nuevoNodo.siguiente = primeroDeLaPila;
        primeroDeLaPila = nuevoNodo;
        cantidadActual++;
        System.out.println("Batería apilada: " + nuevoObjeto);
    }

    // Sacar (Pop)
    public Object sacar() {
        if (primeroDeLaPila == null) return null;
        Object dato = primeroDeLaPila.contenido;
        primeroDeLaPila = primeroDeLaPila.siguiente;
        cantidadActual--;
        return dato;
    }

    // Ver el tope sin sacarlo
    public Object verTope() {
        return primeroDeLaPila == null ? null : primeroDeLaPila.contenido;
    }

    // Mostrar toda la pila (de arriba hacia abajo)
    public void mostrar() {
        if (primeroDeLaPila == null) {
            System.out.println("El cartucho está vacío.");
            return;
        }
        System.out.println("--- Cartucho (tope arriba) ---");
        Nodo actual = primeroDeLaPila;
        while (actual != null) {
            System.out.println("| " + actual.contenido + " |");
            actual = actual.siguiente;
        }
        System.out.println("------------------------------");
        System.out.println("Ocupación: " + cantidadActual + "/" + capacidadMaxima);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PilaLimitada canon = new PilaLimitada(5);
        int contador = 1; // para numerar las baterías
        int opcion = 0;

        do {
            System.out.println("\n===== CAÑÓN DE PLASMA =====");
            System.out.println("1. Apilar batería");
            System.out.println("2. Sacar batería");
            System.out.println("3. Ver batería del tope");
            System.out.println("4. Mostrar cartucho");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");

            try {
                opcion = Integer.parseInt(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                opcion = 0;
            }

            switch (opcion) {
                case 1:
                    if (canon.cantidadActual < canon.capacidadMaxima) {
                        canon.apilar("Batería " + contador);
                        contador++;
                    } else {
                        canon.apilar("Batería " + contador); // muestra el error
                    }
                    break;
                case 2:
                    Object sacada = canon.sacar();
                    if (sacada == null) {
                        System.out.println("No hay baterías para sacar.");
                    } else {
                        System.out.println("Batería sacada: " + sacada);
                    }
                    break;
                case 3:
                    Object tope = canon.verTope();
                    System.out.println(tope == null
                            ? "El cartucho está vacío."
                            : "Tope: " + tope);
                    break;
                case 4:
                    canon.mostrar();
                    break;
                case 5:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción inválida. Elige de 1 a 5.");
            }
        } while (opcion != 5);

        sc.close();
    }
}