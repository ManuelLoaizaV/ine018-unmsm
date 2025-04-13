#include <iostream>
using namespace std;

void Resolver(void) {
    int n;
    cin >> n;

    if (n == 3) {
        cout << "1 3 2" << endl;
        cout << "2 3 1" << endl;
        cout << "3 1 2" << endl;
        return;
    }

    for (int i = n; i >= 1; i--) {
        for (int j = i; j >= 1; j--) {
            cout << j << " ";
        }
        for (int j = n; j > i; j--) {
            cout << j << " ";
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