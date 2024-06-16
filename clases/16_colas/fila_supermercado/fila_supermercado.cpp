#include <cstdlib>
#include <iostream>
#include <queue>

using namespace std;

// Constantes de la simulación
const int TIEMPO_DE_SIMULACION = 28800; // 8 horas en segundos
const int MINIMO_TIEMPO_DE_ATENCION = 150; // 2.5 minutos en segundos
const int MAXIMO_TIEMPO_DE_ATENCION = 360; // 6 minutos en segundos
const long double PROBABILIDAD_LLEGADA = 0.0035L; // Probabilidad de llegada de un cliente en cada segundo

// Función que ejecuta la simulación de la fila de clientes
void EjecutarSimulacion(
    int& total_longitudes_fila,
    int& total_clientes_atendidos,
    int& total_tiempos_espera
) {
    queue<int> fila; // Fila de clientes

    int tiempo_atencion_restante = 0; // Tiempo restante de atención para el cliente actual

    for (int t = 0; t < TIEMPO_DE_SIMULACION; t++) {
        // Determinar si llega un nuevo cliente
        if (rand() / (RAND_MAX + 1.0L) <= PROBABILIDAD_LLEGADA) {
            fila.push(t); // Agregar el tiempo de llegada del cliente a la fila
        }

        // Procesar la atención del cliente actual
        if (tiempo_atencion_restante > 0) {
            tiempo_atencion_restante--;
        } else if (!fila.empty()) {
            // Atender al siguiente cliente en la fila
            total_tiempos_espera += t - fila.front();
            total_clientes_atendidos++;
            tiempo_atencion_restante = MINIMO_TIEMPO_DE_ATENCION + rand() % (MAXIMO_TIEMPO_DE_ATENCION - MINIMO_TIEMPO_DE_ATENCION + 1);
            fila.pop();
        }

        // Sumar la longitud actual de la fila
        total_longitudes_fila += fila.size();
    }
}

// Función que imprime el reporte de la simulación
void ImprimirReporte(
    int total_longitudes_fila,
    int total_clientes_atendidos,
    int total_tiempos_espera
) {
    cout << "Tiempo de simulacion: " << TIEMPO_DE_SIMULACION << " segundos" << endl;
    cout << "Probabilidad de llegada: " << 100 * PROBABILIDAD_LLEGADA << "%" << endl;
    cout << "Tiempo de atencion entre " << MINIMO_TIEMPO_DE_ATENCION << " y " << MAXIMO_TIEMPO_DE_ATENCION << " segundos" << endl;
    cout << "Numero de clientes atendidos: " << total_clientes_atendidos << endl;
    cout << "Tiempo promedio de espera en la fila: " << (long double)total_tiempos_espera / total_clientes_atendidos << endl;
    cout << "Numero promedio de personas en la fila: " << (long double)total_longitudes_fila / TIEMPO_DE_SIMULACION << endl;
}

int main(void) {
    int total_longitudes_fila = 0;
    int total_clientes_atendidos = 0;
    int total_tiempos_espera = 0;

    // Ejecutar la simulación
    EjecutarSimulacion(
        total_longitudes_fila,
        total_clientes_atendidos,
        total_tiempos_espera
    );

    // Imprimir el reporte de la simulación
    ImprimirReporte(
        total_longitudes_fila,
        total_clientes_atendidos,
        total_tiempos_espera
    );

    return 0;
}
