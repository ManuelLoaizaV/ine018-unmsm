// Input: n
// Output: El menor n'umero natural m tal que 1 + 2 + ... + m >= n

// Input: 1
// Output: 1

// Input: 2
// Output: 2

// Input: 3
// Output: 2

// Input: 5
// Output: 3

// Input: 58
// Output: 11

#include <iostream>
using namespace std;

int main(void) {
    int n;
    cin >> n;

    int m = 0;
    int suma = 0;

    while (suma < n) {
        m = m + 1;
        suma = suma + m;
    }

    cout << m << endl;

    return 0;
}