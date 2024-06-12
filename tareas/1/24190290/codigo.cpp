#include <iostream>
using namespace std;

int main () {
  string nombre = "Lionel";
  int longitud = nombre.length();
  cout << nombre << " tiene " << longitud << " caracter(es)." << endl;
  for (int i=0; i < longitud; i++) {
    cout << i << " caracter: " << nombre[i] << endl;
  }
  string apellido = "Messi";
  string nombre_completo = nombre + " " + apellido;
  cout << "Nombre completo: "<< nombre_completo << endl;
  return 0;
}
