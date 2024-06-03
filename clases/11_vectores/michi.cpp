#include <iostream>
#include <vector>
using namespace std;
 
const vector<char> FICHAS = {'X', 'O'};
const char VACIO = '.';

void ImprimirTablero(vector<vector<char>> tablero) {
    cout << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << tablero[i][j];
        }
        cout << endl;
    }
    cout << endl;
}
 
bool Gano(char ficha, vector<vector<char>> tablero) {
    // Verificamos si hay una fila con las tres fichas iguales a la del jugador en cuestión.
    for (int fila = 0; fila < 3; fila++) {
        int coincidencias = 0;
        for (int columna = 0; columna < 3; columna++) {
            if (tablero[fila][columna] == ficha) {
                coincidencias++;
            }
        }
        if (coincidencias == 3) {
            return true;
        }
    }
    
    // Verificamos si hay una columna con las tres fichas iguales a la del jugador en cuestión.
    for (int columna = 0; columna < 3; columna++) {
        int coincidencias = 0;
        for (int fila = 0; fila < 3; fila++) {
            if (tablero[fila][columna] == ficha) {
                coincidencias++;
            }
            if (coincidencias == 3) {
                return true;
            }
        }
    }
    
    // Verificamos si alguna diagonal con las tres fichaes iguales a la del jugador en cuestión.
    bool diagonal_principal = tablero[0][0] == ficha && tablero[1][1] == ficha && tablero[2][2] == ficha;
    bool diagonal_secundaria = tablero[0][2] == ficha && tablero[1][1] == ficha && tablero[2][0] == ficha;
    return diagonal_principal || diagonal_secundaria;
}
 
bool Empate(vector<vector<char>> tablero) {
    int vacios = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (tablero[i][j] == VACIO) {
                vacios++;
            }
        }
    }
    return vacios == 0 && !Gano(FICHAS[0], tablero) && !Gano(FICHAS[1], tablero);
}
 
int main(void) {
    // Construimos el tablero de 3x3 vacío.
    vector<vector<char>> tablero;
    for (int i = 0; i < 3; i++) {
        vector<char> fila;
        for (int j = 0; j < 3; j++) {
            fila.push_back(VACIO);
        }
        tablero.push_back(fila);
    }
    
    // Leemos los nombres de los dos jugadores y los guardamos.
    vector<string> nombres;
    for (int i = 1; i <= 2; i++) {
        string nombre;
        cout << "Ingrese el nombre del jugador " << i << ": ";
        cin >> nombre;
        nombres.push_back(nombre);
    }

    int turno = 0;
 
    while (true) {
        // Imprimimos el estado del tablero antes de cada jugada.
        ImprimirTablero(tablero);

        // Si es que algún jugador ganó, se acabó el juego.
        for (int i = 0; i < 2; i++) {
            if (Gano(FICHAS[i], tablero)) {
                cout << nombres[i] << " es el ganador(a)." << endl;
                return 0;
            }
        }

        // Si es que estamos frente a un empate, también se acabó el juego.
        if (Empate(tablero)) {
            cout << "Empate." << endl;
            break;
        }

        // En otro caso, jugamos un turno adicional.
        turno++;
        cout << "Turno " << turno << " (" << nombres[(turno - 1) % 2] << ")" << endl;
        
        // Actualizamos el tablero con la ficha del jugador correspondiente al turno.
        cout << "Ingrese las coordenadas: ";
        int x, y;
        cin >> x >> y;        
        tablero[x][y] = FICHAS[(turno - 1) % 2];
    }
    
    return 0;
}