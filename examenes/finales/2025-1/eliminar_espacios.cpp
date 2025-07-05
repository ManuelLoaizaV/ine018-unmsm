#include <cassert>
#include <string>

using namespace std;

string EliminarEspacios(string s) {
    string t;
    for (char c : s) {
        if (c != ' ') {
            t += c;
        }
    }
    return t;
}

int main(void) {
    assert(EliminarEspacios("fiee unmsm 2025 1") == "fieeunmsm20251");
    assert(EliminarEspacios(" a 7x  ") == "a7x");
    assert(EliminarEspacios("  ") == "");
    return 0;
}
