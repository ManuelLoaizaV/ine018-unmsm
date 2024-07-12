#include <iostream>
#include <set>
using namespace std;

bool EsSubconjuntoDe(set<int> S, set<int> T) {
    for (int x : S) {
        if (!T.contains(x)) {
            return false;
        }
    }
    return true;
}

int main(void) {
    set<int> A = {1, 2, 3};
    set<int> B = {1, 2, 3, 4, 5};
    set<int> C = {1, 3};
    set<int> D = {1, 3, 6};
    cout << EsSubconjuntoDe(A, B) << endl;
    cout << EsSubconjuntoDe(A, D) << endl;
    cout << EsSubconjuntoDe(C, B) << endl;
    cout << EsSubconjuntoDe(B, A) << endl;
    cout << EsSubconjuntoDe(C, A) << endl;
    cout << EsSubconjuntoDe(A, D) << endl;
    cout << EsSubconjuntoDe(C, D) << endl;
    cout << EsSubconjuntoDe(D, B) << endl;
    return 0;
}