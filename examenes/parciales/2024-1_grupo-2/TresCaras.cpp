#include <iostream>
#include <cstdlib>
using namespace std;

void TresCaras(void) {
    int caras_consecutivas = 0;

    while (caras_consecutivas < 3) {
        if (rand() % 2 == 1) {
            cout << "C ";
            caras_consecutivas++;
        } else {
            cout << "S ";
            caras_consecutivas = 0;
        }
    }

    cout << endl;
    cout << "Tres caras consecutivas :)" << endl;
}

int main(void) {
    for (int i = 0; i < 5; i++) {
        TresCaras();
    }
    return 0;
}