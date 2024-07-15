#include <iostream>

using namespace std;

void SC(int n){
    int suma = 0;
    for(int i = 0; i<=n; i++){
        suma += i*i;
        
    }
    cout<<suma<<endl;

}


int main(void){

    int v;
    cin>>v;

    SC(v);

    return 0;
}
