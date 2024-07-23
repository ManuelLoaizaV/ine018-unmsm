#include <iostream>
using namespace std;

int SumaDeDigitos(int n) {
    if (n < 10) return n;
    return n % 10 + SumaDeDigitos(n / 10);
}

int RaizDigital(int n) {
    if (n < 10) return n;
    return RaizDigital(SumaDeDigitos(n));
}

int main(void) {
    cout << RaizDigital(1729) << endl;
    return 0;
}