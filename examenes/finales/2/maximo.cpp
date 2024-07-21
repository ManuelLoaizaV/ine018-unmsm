#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int Maximo(const vector<int>& v, int n) {
    if (n == 1) return v[0];
    return max(v[n - 1], Maximo(v, n - 1));
}

int main(void) {
    vector<int> v = {1, -2, 50, 6, 9};
    cout << Maximo(v, v.size()) << endl;
    return 0;
}
