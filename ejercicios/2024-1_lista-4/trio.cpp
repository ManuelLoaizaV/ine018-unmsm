#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(void) {
	vector<queue<int>> barajas(3);
	for (int i = 0; i < 3; i++) {
		string movimientos;
		cin >> movimientos;
		for (char movimiento : movimientos) {
			int jugador = movimiento - 'a';
			barajas[i].push(jugador);
		}
	}

	int jugador_actual = 0;
	while (!barajas[jugador_actual].empty()) {
		int siguiente_jugador = barajas[jugador_actual].front();
		barajas[jugador_actual].pop();
		jugador_actual = siguiente_jugador;
	}

	char jugador_ganador = char(int('A') + jugador_actual);
	cout << jugador_ganador << endl;
	return 0;
}
