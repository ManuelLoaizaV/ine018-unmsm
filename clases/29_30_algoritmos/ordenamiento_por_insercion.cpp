#include <iostream>
#include <vector>
using namespace std;

void Ordenar(vector<int>& v) {
    for (int i = 1; i < v.size(); i++) {
        int actual = v[i];
        // Insertamos v[i] en el prefijo ordenado v[0..i - 1]
        int j = i - 1;
        while (j >= 0 && v[j] > actual) {
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = actual;
    }
}

int main(void) {
    return 0;
}
