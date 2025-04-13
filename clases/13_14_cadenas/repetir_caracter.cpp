#include <iostream>
using namespace std;

string RepetirCaracter(char c, int n) {
    string s;
    for (int i = 0; i < n; i++) {
        s += c;
    }
    return s;
}

int main(void) {
    cout << "g" + RepetirCaracter('a', 5) << endl;
    cout << RepetirCaracter('x', 10) << endl;
    cout << "si" << RepetirCaracter('u', 3) << endl;
    return 0;
}