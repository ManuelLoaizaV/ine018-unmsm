#include<iostream>
using namespace std;

int main(void) {
  float n;
  float suma_armonica = 0;
  cout << "Ingrese el valor de la cantidad de términos: ";
  cin >> n;
  float i=1;
  while (i<=n){
    suma_armonica = suma_armonica + 1/i;
    i++;
  }
   float media_armonica = n / suma_armonica;

   cout << "La media armónica de los "<< n << " primeros términos es: " << media_armonica << endl;
  return 0;
}
