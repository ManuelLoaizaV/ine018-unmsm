#include <iostream>
#include <stack>
using namespace std;

int main(void) {
    stack<int> numeros;
    cout << "Ingrese una lista de números enteros, terminando con 0:" << endl;
    
    while (true) {
        cout << "? ";
        int n;
        cin >> n;
        if (n == 0) {
            break;
        }
        numeros.push(n);
    }

    cout << "Estos son los enteros en el orden invertido:" << endl;
    while (!numeros.empty()) {
        cout << numeros.top() << endl;
        numeros.pop();
    }

    return 0;
}