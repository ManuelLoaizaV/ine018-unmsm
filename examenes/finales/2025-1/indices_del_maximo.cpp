#include <vector>
#include <cassert>

using namespace std;

vector<int> IndicesDelMaximo(vector<int> v) {
    int maximo = v[0];
    for (int i = 1; i < v.size(); i++) {
        if (v[i] > maximo) {
            maximo = v[i];
        }
    }
    vector<int> indices;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] == maximo) {
            indices.push_back(i);
        }
    }
    return indices;
}

int main(void) {
    assert(IndicesDelMaximo({7, 23, 19, 23}) == (vector<int>{1, 3}));
    assert(IndicesDelMaximo({-17}) == vector<int>{0});
    assert(IndicesDelMaximo({-11, -2, -2, -2, -3}) == (vector<int>{1, 2, 3}));
    return 0;
}