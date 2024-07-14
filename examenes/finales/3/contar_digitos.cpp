#include <iostream>
using namespace std;

int ContarDigitos(int n) {
    if (n < 10) return 1;
    return 1 + ContarDigitos(n / 10);
}

int main(void) {
    cout << ContarDigitos(8546587) << endl;
    cout << ContarDigitos(123) << endl;
    cout << ContarDigitos(7) << endl;
    cout << ContarDigitos(987654321) << endl;
    return 0;
}