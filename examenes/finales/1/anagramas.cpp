#include <cctype>
#include <iostream>
#include <vector>
using namespace std;

vector<int> Frecuencias(string s) {
    vector<int> frecuencias(26, 0);
    for (char c : s) {
        frecuencias[tolower(c) - 'a']++;
    }
    return frecuencias;
}

bool Anagrama(string s, string t) {
    return Frecuencias(s) == Frecuencias(t);
}

int main(void) {
    cout << Anagrama("enlodar", "leandro") << endl;
    cout << Anagrama("ababa", "abbba") << endl;
    cout << Anagrama("insecto", "incesto") << endl;
    cout << Anagrama("zzzz", "zzz") << endl;
    cout << Anagrama("enamoramientos", "armoniosamente") << endl;
    return 0;
}