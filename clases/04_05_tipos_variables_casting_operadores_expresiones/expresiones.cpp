#include <iostream>
using namespace std;

int main(void) {
    double x = 7;
    double y = 3;
    double z = x / y;
    cout << z << endl;

    int b = 9 + 3 * 7 - 1;
    cout << b << endl;

    int a = 5 + 3 / 4;
    cout << a << endl;

    double c = 8.0 / 3.0 * 2.0;
    cout << c << endl;

    double d = 8 / 3 * 2.0;
    cout << d << endl;

    bool e = (5 == 7);
    cout << std::boolalpha << e << endl;

    bool f = 5 != 7;
    cout << std::boolalpha << f << endl;

    bool g = 0 >= 0;
    cout << std::boolalpha << g << endl;

    bool h = 5.01 != 5;
    cout << std::boolalpha << h << endl;

    bool i = 4 != 5 || 5 < 3 || 10 > 1 || false;
    cout << std::boolalpha << i << endl;

    bool j = i && 5 >= 4 && true && !h;
    cout << std::boolalpha << j << endl;

    bool k = 6 > 9 || 5 > 4 && 3 < 10;
    cout << std::boolalpha << k << endl;

    bool m = 1 + 2 * 3 != (1 + 2) * 3;
    cout << std::boolalpha << m << endl;

    bool n = 5 < 9 || (7 != 7);
    cout << std::boolalpha << n << endl;
    return 0;
}