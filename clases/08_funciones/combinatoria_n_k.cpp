#include <iostream>
using namespace std;

long long Factorial(int n) {
    long long producto = 1LL;
    for (long long i = 1LL; i <= n; i++) {
        producto *= i;
    }
    return producto;
}

int nCk(int n, int k) {
    return Factorial(n) / (Factorial(k) * Factorial(n - k));
}

int main(void) {
    cout << nCk(7, 3) << endl;  // 35
    cout << nCk(10, 4) << endl;  // 210
    cout << nCk(4, 0) << endl;  // 1
    cout << nCk(8, 3) << endl;  // 56
    return 0;
}