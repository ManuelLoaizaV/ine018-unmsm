#include <iostream> 
#include <string>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main(){
int min, max;
int intento;
char respuesta; 


cout<<"Intentare adivinar un numero que tu elijas."<<endl;
cout<<"Cuando indique el numero tu deberas indicar:"<<endl<<
              "\t= si acierto al numero que tu quieres que adivine\n"
              "\t> si el numero que tu quieres que adivine es mayor al que moestre.\n"
              "\t< si el numero que tu quieres que adivine es menor al que muestre.\n";
cout<<"Dime el numero minimo: ";cin>>min;
cout<<"Dime el numero maximo: ";cin>>max;


  if(min<max){

float  numeroIntentos = ceil(log2(max-min+1));

cout<<"\nESTA BIEN. Adivinare tu numero en no mas de "<<numeroIntentos<<" intentos.";
cout<<"\nPresiona cualquier tecla(enter xd) cuando quieras comenzar...";getchar();getchar();


  for(intento=1;intento<=numeroIntentos;intento++){

    cout<<"\nIntento "<<intento<<" -> El numero es..."<<(min+max)/2; cout<<": ";cin>>respuesta; 

    switch(respuesta) {
      case '=': cout<<"\nte ganee!!!";  break;
      case '>': 
        min= ((min+max)/2) +1;
        break;
      case '<': 
        max= ((min+max)/2)-1;
        break;
      default: 
        cout<<"RESPUESTA INVALIDA. Un game over para ti...";
      return 0;
    }
    if(min>max){cout<<"ESTAS HACIENDO TRAMPA TONTO";break;}
  }
  }else {cout <<"NO HAGAS TRAMPA OE";}



  system("pause");
  return 0;
}
