#include <iostream>
#include <vector>
using namespace std;

void ImprimirFrecuencias(string s) {
    int n = s.size();
    vector<int> frecuencias;
    for (int i = 0; i < 26; i++) {
        frecuencias.push_back(0);
    }

    for (int i = 0; i < n; i++) {
        char c = s[i];
        if ('A' <= c && c <= 'Z') {
            c = c - 'A' + 'a';
        }
        if ('a' <= c && c <= 'z') {
            frecuencias[c - 'a']++;
        }
    }

    cout << s << endl;
    for (int i = 0; i < 26; i++) {
        if (frecuencias[i] == 0) {
            continue;
        }
        char actual = 'a' + i;
        cout << actual << " = " << frecuencias[i] << endl;
    }

    cout << endl;
}

int main(void) {
    // ImprimirFrecuencias("esternocleidomastoideo");
    // ImprimirFrecuencias("ciclopentanoperhidrofenantreno");
    // ImprimirFrecuencias("esternocleidomastoideociclopentanoperhidrofenantreno");
    // ImprimirFrecuencias("the quick brown fox jumps over the lazy dog");
    ImprimirFrecuencias("Miguel");
    ImprimirFrecuencias("alejandro");
    ImprimirFrecuencias("UNMSM");
    return 0;
}