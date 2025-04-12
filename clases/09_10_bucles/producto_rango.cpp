#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
    int l, r;
    cout << "Ingrese dos enteros que representen [l, r]: ";
    cin >> l >> r;

    if (l > r) {
        int k = l;
        l = r;
        r = k;
    }

    int producto = 1;
    for (int i = l; i <= r; i = i + 1) {
        producto = producto * i;
    }

    cout << "Producto: " << producto << endl;

    return 0;
}