#include <cassert>
#include <set>
#include <vector>

using namespace std;

bool TodosDiferentes(vector<int> v) {
    set<int> s;
    for (int e : v) {
        s.insert(e);
    }
    return v.size() == s.size();
}

int main(void) {
    assert(TodosDiferentes({3, 1, 4, 5, 9}));
    assert(!TodosDiferentes({3, 1, 4, 1, 5}));
    assert(!TodosDiferentes({42, 42}));
    assert(TodosDiferentes({2025}));
    assert(TodosDiferentes({}));
    return 0;
}