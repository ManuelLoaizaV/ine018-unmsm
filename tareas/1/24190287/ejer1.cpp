#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];
    int transpuesta[3][3];

    cout << "Ingrese los elementos de la matriz (3x3):" << endl;

    for (int i=0; i<3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> matriz[i][j];
        }
    }

    for (int i=0; i<3; ++i) {
        for (int j = 0; j < 3; ++j) {
            transpuesta[j][i] = matriz[i][j];
        }
    }

    cout << "Matriz transpuesta:" << endl;
    for (int i=0; i<3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << transpuesta[i][j] << " ";
        }
        cout << endl;
    }

}