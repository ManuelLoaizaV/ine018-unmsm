#include <iostream>
using namespace std;

bool EsSubcadenaPalindroma(string& s, int l, int r) {
    // Casos base: Todas las cadenas de tamaño 0 o 1 son palíndromas.
    if (l >= r) {
        return true;
    }
    // Relación de recurrencia: Una cadena es palíndroma si
    // su primer y último caracter coinciden y
    // la subcadena restante es palíndroma.
    return s[l] == s[r] && EsSubcadenaPalindroma(s, l + 1, r - 1);
}

bool EsPalindroma(string s) {
    return EsSubcadenaPalindroma(s, 0, (int)s.size() - 1);
}

int main(void) {
    cout << EsPalindroma("anitalavalatina") << endl;
    cout << EsPalindroma("manuel") << endl;
    cout << EsPalindroma("reconocer") << endl;
    cout << EsPalindroma("xyz") << endl;
    cout << EsPalindroma("oso") << endl;
    cout << EsPalindroma("abacdba") << endl;
    cout << EsPalindroma("a") << endl;
    return 0;
}