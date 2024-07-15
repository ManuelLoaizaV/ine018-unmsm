#include <iostream>

using namespace std;

int main(void){
 int dia;
 cout << "¿que dia es mi cumpleaños?, tienes 3 intentos"<< endl;

 for(int i=0; i<=2; i++ ){
  cin >> dia;
    if (dia == 24){
      cout << "sii,ese es mi cumpleeaños, :D"<< endl;
   }else if (dia > 0 && dia <=23 || dia >24 && dia <= 31 ){
      cout << "sigue intentando :P"<< endl;
   }else {
      cout << "no estas ni cerca xd"<< endl;
}
}
return 0;
}