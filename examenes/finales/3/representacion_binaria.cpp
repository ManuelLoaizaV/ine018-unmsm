#include <iostream>
#include <stack>

using namespace std;

void RepresentacionBinaria(int n) {
    stack<int> bits;
    while (n > 0) {
        bits.push(n % 2);
        n /= 2;
    }
    while (!bits.empty()) {
        cout << bits.top();
        bits.pop();
    }
    cout << endl;
}

int main(void) {
    RepresentacionBinaria(10);
    RepresentacionBinaria(19);
    RepresentacionBinaria(32);
    RepresentacionBinaria(73);
    return 0;
}