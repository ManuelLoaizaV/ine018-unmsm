#include <iostream>
using namespace std;

int main(void){
    int a ; 
    int b ;
    int c ;
    cin >> a >> b >> c ;
    if((a+b)/2==c){
        cout << "Si existe punto medio y es " << c ;
    } else if((a+c)/2==b){
        cout << "Si existe punto medio y es " << b ;
    } else if((b+c)/2==a){
        cout << "Si existe punto medio y es " << a ;
    } else {
        cout << "No existe punto medio" << endl;
    }
    return 0;
}