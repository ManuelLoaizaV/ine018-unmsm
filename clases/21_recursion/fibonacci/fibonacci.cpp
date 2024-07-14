#include <iostream>
using namespace std;

long long f(int n) {
    // Casos base: f(1) = f(2) = 1
    if (n <= 2) {
        return 1LL;
    }
    // Relación de recurrencia: f(n) = f(n - 1) + f(n - 2)
    return f(n - 1) + f(n - 2);
}

int main(void) {
    cout << "f(1) = " << f(1) << endl;
    cout << "f(5) = " << f(5) << endl;
    cout << "f(10) = " << f(10) << endl;
    cout << "f(20) = " << f(20) << endl;
    cout << "f(40) = " << f(40) << endl;
    return 0;
}