#include <iostream>
using namespace std;

int Elevar(int n, int k) {
    if (k == 0) {
        return 1;
    }
    return n * Elevar(n, k - 1);
}

int main(void) {
    cout << Elevar(5, 0) << endl;
    cout << Elevar(5, 1) << endl;
    cout << Elevar(5, 3) << endl;
    return 0;
}