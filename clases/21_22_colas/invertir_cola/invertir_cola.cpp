#include <iostream>
#include <queue>
#include <stack>
using namespace std;

void ImprimirCola(queue<string> cola) {
    while (!cola.empty()) {
        cout << cola.front() << " ";
        cola.pop();
    }
    cout << endl;
}

void InvertirCola(queue<string>& cola) {
    stack<string> pila;

    while (!cola.empty()) {
        string cabeza = cola.front();
        cola.pop();
        pila.push(cabeza);      
    }

    while (!pila.empty()) {
        string tope = pila.top();
        pila.pop();
        cola.push(tope);
    }
}

int main(void) {
    queue<string> alumnos;

    alumnos.push("Jake");
    alumnos.push("Alejandro");
    alumnos.push("Abel");
    alumnos.push("Angel");
    alumnos.push("Rosa");

    ImprimirCola(alumnos);    
    InvertirCola(alumnos);
    ImprimirCola(alumnos);

    return 0;
}