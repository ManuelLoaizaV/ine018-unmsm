#include <iostream>

using namespace std;

int main() {
    int edad_mental , edad_cronologica;
    cout << "Ingrese su edad mental: "; 
    cin >> edad_mental;
    cout << "Ingrese su edad cronologica: ";
    cin >> edad_cronologica;
//Calcular el cociente intelectual
    double CI = (double(edad_mental) / double(edad_cronologica)) * 100;
    cout << "Su Cociente Intelectual es: " << CI << std::endl;

    return 0;
}
