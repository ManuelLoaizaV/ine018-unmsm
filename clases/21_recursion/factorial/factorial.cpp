#include <iostream>
using namespace std;

long long f(long long n) {
    // Caso base: 0! = 1
    if (n == 0) {
        return 1LL;
    }
    // Relación de recurrencia: n! = n * (n - 1)!
    return n * f(n - 1LL);
}

int main(void) {
    cout << f(6LL) << endl;
    return 0;
}