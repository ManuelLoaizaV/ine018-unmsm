#include <iostream>
using namespace std;
int main(void){
  int a;
  while(true) {
    cout << "Ingrese un número de tres cifras a invertir: ";
    cin >> a;
    if (a >= 100 && a <= 999) {
      int c3 = (a % 10);
      int c2 = (a % 100) / 10;
      int c1 = (a / 100);
      cout << "El número invertido es: "<< c3 << c2 << c1 << endl;
        break;
        } else {
      cout << "El número no es de tres cifras, vuelva a intentarlo por favor." <<endl;
    }
  }
  return 0;
}