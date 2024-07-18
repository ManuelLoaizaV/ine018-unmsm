#include <iostream>
#include <stack>
#include <string>
using namespace std;

void ComandoDeAyuda(void) {
    cout << "Ingrese expresiones en RPN," << endl;
    cout << "en donde los operadores aparecen luego de" << endl;
    cout << "los operandos sobre los cuales serán aplicados." << endl;
    cout << "Cada línea consiste de número,";
    cout << " un operador,";
    cout << " o uno de los siguientes comandos:" << endl;
    cout << "Q: Terminar el programa" << endl;
    cout << "H: Mostrar este mensaje de ayuda" << endl;
    cout << "C: Limpiar la memoria de la calculadora" << endl;
}

bool EsOperador(string s) {
    return s == "+" || s == "-" || s == "*" || s == "/";
}

void AplicarOperador(string operador, stack<double>& memoria) {
    double resultado;
    double derecha = memoria.top();
    memoria.pop();
    double izquierda = memoria.top();
    memoria.pop();
    if (operador == "+") {
        resultado = izquierda + derecha;
    } else if (operador == "-") {
        resultado = izquierda - derecha;
    } else if (operador == "*") {
        resultado = izquierda * derecha;
    } else if (operador == "/") {
        resultado = izquierda / derecha;
    }
    cout << resultado << endl;
    memoria.push(resultado);
}

int main(void) {
    cout << "Simulación de calculadora RPN (ingrese H para ayuda)" << endl;
    stack<double> memoria;
    while (true) {
        string entrada;
        cin >> entrada;
        if (entrada == "Q") {
            break;
        } else if (entrada == "C") {
            memoria = stack<double>();
        } else if (entrada == "H") {
            ComandoDeAyuda();
        } else if (EsOperador(entrada)) {
            AplicarOperador(entrada, memoria);
        } else {
            memoria.push(stod(entrada));
        }
    }
    return 0;
}