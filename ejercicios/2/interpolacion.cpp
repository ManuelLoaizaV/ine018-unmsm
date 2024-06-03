#include <iostream>
using namespace std;

void Resolver(void) {
    int n;
    cin >> n;
    for (int i = 0; i < 2 * n; i++) {
        for (int j = 0; j < 2 * n; j++) {
            if ((i / 2) % 2 == (j / 2) % 2) {
                cout << "#";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}

int main(void) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        Resolver();
    }
    return 0;
}