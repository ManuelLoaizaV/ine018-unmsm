#include <iostream>
using namespace std;

void Resolver(void) {
    long long n, k;
    cin >> n >> k;
    
    long long operaciones = 0;

    while (n > 0) {
        if (n % k == 0) {
            n /= k;
            operaciones++;
        } else {
            operaciones += n % k;
            n -= n % k;
        }
    }

    cout << operaciones << endl;
}

int main(void) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        Resolver();
    }
    return 0;
}