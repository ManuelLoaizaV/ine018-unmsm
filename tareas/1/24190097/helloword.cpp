#include <iostream>
using namespace std;
int main(void){
  int opciones, precio, piezas ;
  cout << "\nBienvenido a la tienda de Belen, elija una opcion: " << endl;
  cout << "1.Quiero un tradicional" << endl ;
  cout << "2.Quiero un deluxe" << endl ;
  cout << "3.Quiero piezas de pollo" << endl ;
  cout << "Ingrese la opcion que desea: " ; cin >> opciones ;
  switch (opciones){
    case 1: cout << "El tiempo de espera estimado es 7 minutos " ; break ;
    case 2: cout << "El tiempo de espera estimado es 8 minutos " ; break ;
    case 3: cout << "Cuantas piezas de pollo desea? " ;
      cin >> piezas ;
      precio=6*piezas ;
      cout << "El precio total es de " << precio << " soles " ; break ;

  }
    return 0 ;
}