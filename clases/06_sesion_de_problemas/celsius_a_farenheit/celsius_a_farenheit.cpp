#include <iostream>
#include <iomanip>
using namespace std;

int main(void) {
    double c;
    cout << "Ingrese la temperatura en Celsius: ";
    cin >> c;
    
    double f = 9 * c / 5 + 32;

    cout << "La temperatura en Farenheit es " << fixed << setprecision(8) << f << endl;
    return 0;
}