#include <iostream>
#include <set>
using namespace std;

set<int> Diferencia(const set<int>& S, const set<int>& T) {
    set<int> R;
    for (int s : S) {
        if (!T.contains(s)) {
            R.insert(s);
        }
    }
    return R;
}

void ImprimirDiferencia(const set<int>& S, const set<int>& T) {
    set<int> R = Diferencia(S, T);
    for (int r : R) {
        cout << r << ' ';
    }
    cout << endl;
}

int main(void) {
    set<int> A = {1, 2, 3};
    set<int> B = {4, 5, 6};
    set<int> C = {3, 4, 5};
    set<int> D = {1, 2, 6};

    ImprimirDiferencia(A, B);  // A
    ImprimirDiferencia(A, C);  // {1, 2}
    ImprimirDiferencia(A, D);  // {3}
    return 0;
}