#include <iostream>
using namespace std;

// imprimir numeros en grupos de 4
void process_for_impares(int p){
    for (int i=1; i<=p; i+=8) {
      if (i+4>p){
        cout << i << "-" << i + (p-i);
      } else {
        cout << i << "-" << i+3 << endl;
      }
  }
}

// imprimir numeros en grupos de 4 omitidos
void process_for_pares(int p){
    for (int i=1; i<=p; i+=8) {
      if (i+7>p){
        if (i%4==1){
        } else {
          cout << i << "-" << i + (p-i);
        }
      } else {
        cout << i+4 << "-" << i+7 << endl;
      }
  }
}

int main() {
  int n;
  cin >> n;
  cout << "páginas impares: "; 
  process_for_impares(n);
  cout << endl;
  cout << "páginas pares: ";
  process_for_pares(n);
}