#include<iostream>
#include<string>

using namespace std;

int main(){
    string cadena;
    cout<<"Ingrese una palabra: "<<endl;
    cin>>cadena; cout<<endl;
    int longitud=cadena.size();

    for(int i=0;i<longitud;i++){
        swap(cadena[i],cadena[longitud-1]);
        longitud--;
    }
    cout<<"La forma invertida de la palabbra ingresada es: "<<endl;
    cout<<cadena<<endl;
    
    return 0;
}