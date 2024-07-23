#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

/*
 * n[0]: Tamaño fijo del vector v.
 * n[1]: Número de elementos en la primera pila. Inicialmente cero.
 * n[2]: Número de elementos en la segunda pila. Inicialmente cero.
 * No olvide inicializar este vector antes de manipular las pilas.
 */
vector<int> n;

/*
 * Vector de tamaño fijo que contendrá los elementos de las dos pilas.
 * No olvide redimensionarlo una vez inicializado el vector n.
 */
vector<int> v;


// Inserta x en la i-ésima pila.
void Push(int i, int x) {
    if (n[1] + n[2] == n[0]) {
        throw runtime_error("Memoria insuficiente.");
    }
    if (i == 1) {
        v[n[1]] = x;
    } else {
        v[n[0] - 1 - n[2]] = x;
    }
    n[i]++;
}

// Elimina el valor en el tope de la i-ésima pila.
void Pop(int i) {
    if (n[i] == 0) {
        throw runtime_error("No se puede desapilar de una pila vacía.");
    }
    n[i]--;
}

// Retorna el valor en el tope de la i-ésima pila sin eliminarlo.
int Top(int i) {
    if (n[i] == 0) {
        throw runtime_error("No se puede obtener el tope de una pila vacía.");
    }
    if (i == 1) return v[n[1] - 1];
    return v[n[0] - n[2]];
}

// Retorna el número de elementos actualmente en la i-ésima pila.
int Size(int i) {
    return n[i];
}

// Retorna true si la i-ésima pila está vacía.
bool Empty(int i) {
    return n[i] == 0;
}

int main(void) {
    n = {10, 0, 0};
    v.resize(n[0]);
    Push(1, 10);
    Push(1, 20);
    Push(2, 30);
    Push(1, 40);
    Push(2, 50);
    Push(2, 60);
    Push(2, 70);
    Push(1, 80);
    Push(2, 90);
    Push(2, 100);

    cout << "Tope de la primera pila: " << Top(1) << endl;
    cout << "Tope de la segunda pila: " << Top(2) << endl;

    cout << "Desapilamos un elemento de la primera pila." << endl;
    Pop(1);
    cout << "Nuevo tope de la primera pila: " << Top(1) << endl;

    cout << "Imprimimos la segunda pila: ";
    while (!Empty(2)) {
        cout << Top(2) << ' ';
        Pop(2);
    }
    cout << endl;
    return 0;
}