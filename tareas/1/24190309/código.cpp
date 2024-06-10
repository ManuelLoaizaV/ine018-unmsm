#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "El numero de sumandos es: "<<endl;
    cin >> n;
    int suma = 0;
    for (int i = 1; i <=n; i++){
        suma = suma + i*(i+1);
    }
    cout << "El resultado de la sumatoria de n(n+1) es : " << suma << endl;
    return 0;
}