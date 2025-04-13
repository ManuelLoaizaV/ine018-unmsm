#include <iostream>
using namespace std;

bool EsPrimo(int n) {
    // Contamos el número de divisores de n.
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cnt++;
        }
    }

    // n es primo si y solo si tiene dos divisores.
    return cnt == 2;
}

int IesimoPrimo(int i) {
    int primos_encontrados = 0;
    int candidato = 0;

    // Mientras no hayamos encontrado suficientes primos ...
    while (primos_encontrados < i) {
        // Nos movemos al siguiente candidato.
        candidato++;
        // Y de ser primo, contamos uno más.
        if (EsPrimo(candidato)) {
            primos_encontrados++;
        }
    }

    return candidato;
}

int main(void) {
    cout << IesimoPrimo(10) << endl;  // 29
    cout << IesimoPrimo(1) << endl;  // 2
    cout << IesimoPrimo(5) << endl;  // 11
    cout << IesimoPrimo(11) << endl;  // 31
    cout << IesimoPrimo(100) << endl;  // 541
    return 0;
}