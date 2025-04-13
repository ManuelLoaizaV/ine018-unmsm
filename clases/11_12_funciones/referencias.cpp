#include <iostream>
using namespace std;

void AsignarCero(int& x) {
    x = 0;
}

int main(void) {
    int n = 1024;
    AsignarCero(n);
    cout << n << endl;
    return 0;
}