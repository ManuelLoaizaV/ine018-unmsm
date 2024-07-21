#include <iostream>
#include <set>

using namespace std;

bool SonConjuntosDisjuntos(const set<int>& S, const set<int>& T) {
    for (int s : S) {
        if (T.contains(s)) {
            return false;
        }
    }
    return true;
}

int main(void) {
    set<int> A = {1, 2, 3};
    set<int> B = {4, 5, 6};
    set<int> C = {3, 4, 5};
    set<int> D = {1, 2, 6};
    cout << SonConjuntosDisjuntos(A, B) << endl;
    cout << SonConjuntosDisjuntos(A, C) << endl;
    cout << SonConjuntosDisjuntos(C, D) << endl;
    cout << SonConjuntosDisjuntos(B, D) << endl;
    return 0;
}