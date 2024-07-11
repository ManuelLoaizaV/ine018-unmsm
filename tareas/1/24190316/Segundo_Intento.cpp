#include <iostream>
#include <string>
using namespace std;

void comparar(string s, string t) {
  if (s == t) {
    cout << s << " y " << t << " son iguales" << endl;
  } else if (s < t) {
    cout << s << " es menor que " << t << endl;
  } else {
    cout << s << " es mayor que " << t << endl;
  }
}


int main() {
  string nombre = "Raul";

  int longitud = nombre.length();

  cout << nombre << " tiene " << longitud << " caracteres." << endl;

  for (int i = 0; i < longitud; i++) {
    cout << i << "esimo caracter "<< nombre[i] << endl;
  }

  string apellido = "Alarcon";

  string nombre_completo = nombre + " " + apellido;
  cout << "Nombre completo: " << nombre_completo << endl;

comparar("domingo","jueves");  
}