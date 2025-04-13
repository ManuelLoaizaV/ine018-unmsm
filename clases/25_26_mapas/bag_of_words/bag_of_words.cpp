#include <cctype>
#include <iostream>
#include <map>
using namespace std;

void LimpiarTexto(string& texto) {
    for (int i = 0; i < texto.size(); i++) {
        if (isalpha(texto[i])) {
            texto[i] = tolower(texto[i]);
        } else {
            texto[i] = ' ';
        }
    }
}

int main(void) {
    string texto = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content, And tender churl mak'st waste in niggarding: Pity the world, or else this glutton be, To eat the world's due, by the grave and thee.";
    LimpiarTexto(texto);

    map<string, int> frecuencias;
    for (int i = 0; i < texto.size(); i++) {
        if (texto[i] == ' ') {
            continue;
        }
        int j = i;
        while (j < texto.size() && texto[j] != ' ') {
            j++;
        }
        string palabra = texto.substr(i, j - i);
        if (frecuencias.contains(palabra)) {
            frecuencias[palabra]++;
        } else {
            frecuencias[palabra] = 1;
        }
        i = j;
    }

    for (pair<string, int> p : frecuencias) {
        string palabra = p.first;
        int frecuencia = p.second;
        cout << "La palabra " << palabra << " aparece " << frecuencia << " veces." << endl;
    }
    return 0;
}