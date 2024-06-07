#include <iostream>
using namespace std;
int main(void){
    cout << "Ingrese n:" << endl;
    int n;
    cin >> n;
    int sumatoria_primeros_cuadrados = (n*(n+1)*((2*n)+1))/6;
    cout << "La sumatoria de los " << n << " primeros cuadrados es: " << endl << sumatoria_primeros_cuadrados;
    return 0;
}