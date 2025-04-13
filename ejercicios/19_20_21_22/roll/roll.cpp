#include <iostream>
#include <queue>
#include <stack>
using namespace std;

void ImprimirPila(stack<char> pila) {
    cout << endl;
    while (!pila.empty()) {
        cout << pila.top() << endl;
        pila.pop();
    }
    cout << endl;
}

void InvertirCola(queue<char>& cola) {
    stack<char> pila;
    while (!cola.empty()) {
        pila.push(cola.front());
        cola.pop();
    }
    while (!pila.empty()) {
        cola.push(pila.top());
        pila.pop();
    }
}

void Roll(stack<char>& pila, int n, int k) {
    cout << "roll " << n << " " << k << endl;
    queue<char> ultimos;
    for (int i = 0; i < n; i++) {
        ultimos.push(pila.top());
        pila.pop();
    }

    int offset = k % n;
    for (int i = 0; i < offset; i++) {
        ultimos.push(ultimos.front());
        ultimos.pop();
    }
    
    InvertirCola(ultimos);

    while (!ultimos.empty()) {
        pila.push(ultimos.front());
        ultimos.pop();
    }
}

int main(void) {
    stack<char> pila;
    pila.push('A');
    pila.push('B');
    pila.push('C');
    pila.push('D');

    ImprimirPila(pila);

    Roll(pila, 4, 1);
    ImprimirPila(pila);

    Roll(pila, 3, 2);
    ImprimirPila(pila);

    Roll(pila, 2, 4);
    ImprimirPila(pila);

    return 0;
}