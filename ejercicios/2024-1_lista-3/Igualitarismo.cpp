#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int Costo(int x, vector<int>& a) {
    int costo = 0;
    for (int y : a) {
        costo += (x - y) * (x - y);
    }
    return costo;
}

int main(void) {
    int n;
    cin >> n;

    int minimo = 101;
    int maximo = -101;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        minimo = min(minimo, a[i]);
        maximo = max(maximo, a[i]);
    }

    int minimo_costo = Costo(minimo, a);

    for (int x = minimo + 1; x <= maximo; x++) {
        minimo_costo = min(minimo_costo, Costo(x, a));
    }

    cout << minimo_costo << endl;
    
    return 0;
}