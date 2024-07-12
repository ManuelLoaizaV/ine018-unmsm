#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> tiempos(n);

    int tiempo_total = 0;
    for (int i = 0; i < n; i++) {
        cin >> tiempos[i];
        tiempo_total += tiempos[i];
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int partido;
        cin >> partido;
        int nuevo_tiempo;
        cin >> nuevo_tiempo;
        int nuevo_tiempo_total = tiempo_total - tiempos[partido - 1] + nuevo_tiempo;
        cout << nuevo_tiempo_total << endl;
    }
    return 0;
}