#include <iostream>
using namespace std;

bool EsPrimo(int n){
    if(n<=1){
        return false;
    }

    if(n%2==0 && n != 2){
        return false;
    }
    if(n%3==0 && n!=3){
        return false;
    }
    if(n%5==0 && n!=5){
        return false;
    }
    if(n%7==0 && n!=7){
        return false;
    
}
    return true;
}
int main(){
    int n;
   
    cout<< "ingrese un numero: ";
    cin>>n;
        if(EsPrimo(n)){
        cout<<n<<" Es primo"<<endl;
        } else{
        cout<<n<<" No es primo";
}

return 0;
}