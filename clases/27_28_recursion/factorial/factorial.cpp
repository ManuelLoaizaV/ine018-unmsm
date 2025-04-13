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
    cout << "3! = " << f(3LL) << endl;
    cout << "6! = " << f(6LL) << endl;
    cout << "9! = " << f(9LL) << endl;
    return 0;
}