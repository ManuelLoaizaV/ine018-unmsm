#include <vector>
#include <cassert>

using namespace std;

vector<int> Ordenar(vector<int> v) {
    vector<int> frecuencias(10, 0);
    for (int e : v) {
        frecuencias[e]++;
    }
    vector<int> ordenado;
    for (int i = 0; i < 10; i++) {
        for (int j = 1; j <= frecuencias[i]; j++) {
            ordenado.push_back(i);
        }
    }
    return ordenado;
}

int main(void) {
    assert(
        Ordenar({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8})
        ==
        (vector<int>{1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 9, 9})
    );
    assert(Ordenar({2, 1, 3}) == (vector<int>{1, 2, 3}));
    return 0;
}
