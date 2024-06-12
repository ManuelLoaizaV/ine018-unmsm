#include <cstdlib>
#include <iostream>
#include <queue>
using namespace std;

// Constantes
const int TIEMPO_DE_SIMULACION = 43200;
const long double PROBABILIDAD_DE_LLEGADA = 0.005L;
const int TIEMPO_MINIMO_DE_ATENCION = 60;
const int TIEMPO_MAXIMO_DE_ATENCION = 300;

void CorrerSimulacion(
	int& numero_clientes_atendidos,
	int& suma_tiempos_de_espera,
	int& suma_longitudes_de_fila
) {
	// Cola que representa a los clientes esperando su turno en la caja.
	// Cada cliente estará representado por el instante de tiempo en el que llegó a la cola.
	queue<int> clientes;

	int tiempo_restante_de_atencion = 0;
    numero_clientes_atendidos = 0;
    suma_tiempos_de_espera = 0;
    suma_longitudes_de_fila = 0;
	
	// Simulamos cada segundo. Estos están en el intervalo [1, 43200].
	for (int t = 1; t <= TIEMPO_DE_SIMULACION; t++) {
		// Llega un cliente aleatoriamente
		if (rand() / (RAND_MAX + 1.0L) <= PROBABILIDAD_DE_LLEGADA) {
			clientes.push(t);
		}
		
		if (tiempo_restante_de_atencion > 0) {
			// Decrementamos en uno el tiempo de atencion
			tiempo_restante_de_atencion--;
		} else if (!clientes.empty()) {
			// Atendemos a un cliente
			suma_tiempos_de_espera += t - clientes.front();
			clientes.pop();
            numero_clientes_atendidos++;
			tiempo_restante_de_atencion = rand() % (TIEMPO_MAXIMO_DE_ATENCION - TIEMPO_MINIMO_DE_ATENCION + 1) + TIEMPO_MINIMO_DE_ATENCION;
		}
		suma_longitudes_de_fila += clientes.size();
	}
}

void ImprimirReporte(
    int numero_clientes_atendidos,
    int suma_tiempos_de_espera,
    int suma_longitudes_de_fila
) {
    cout << "Resultados de la simulación dadas las siguientes constantes:" << endl;
	cout << "TIEMPO DE SIMULACIÓN: " << TIEMPO_DE_SIMULACION << " s" << endl;
	cout << "PROBABILIDAD DE LLEGADA: " << 100 * PROBABILIDAD_DE_LLEGADA << '%' << endl;
	cout << "DURACIÓN DE ATENCIÓN: [" << TIEMPO_MINIMO_DE_ATENCION << ", " << TIEMPO_MAXIMO_DE_ATENCION << "] s" << endl;
    cout << endl;
    cout << "Clientes atendidos: " << numero_clientes_atendidos << endl;
    long double tiempo_de_espera_promedio = (long double)suma_tiempos_de_espera / numero_clientes_atendidos;
    cout << "Tiempo de espera promedio: " << tiempo_de_espera_promedio << endl;
    long double longitud_promedio_fila = (long double)suma_longitudes_de_fila / TIEMPO_DE_SIMULACION;
    cout << "Longitud promedio de la fila: " << longitud_promedio_fila << endl;
}

int main(void) {
	int numero_clientes_atendidos = 0;
	int suma_tiempos_de_espera = 0;
	int suma_longitudes_de_fila = 0;
	CorrerSimulacion(numero_clientes_atendidos, suma_tiempos_de_espera, suma_longitudes_de_fila);
    ImprimirReporte(numero_clientes_atendidos, suma_tiempos_de_espera, suma_longitudes_de_fila);
	return 0;
}