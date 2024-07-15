#include <cctype>
#include <iostream>
#include <map>
#include <utility>
using namespace std;

bool EstaEnMorse(string texto) {
    for (char c : texto) {
        if (c == ' ') {
            continue;
        }
        if (isalpha(c)) {
            return false;
        }
    }
    return true;
}

int main(void) {
    map<char, string> letra_a_morse;
    letra_a_morse['A'] = ".-";
    letra_a_morse['B'] = "-...";
    letra_a_morse['C'] = "-.-.";
    letra_a_morse['D'] = "-..";
    letra_a_morse['E'] = ".";
    letra_a_morse['F'] = "..-.";
    letra_a_morse['G'] = "--.";
    letra_a_morse['H'] = "....";
    letra_a_morse['I'] = "..";
    letra_a_morse['J'] = ".---";
    letra_a_morse['K'] = "-.-";
    letra_a_morse['L'] = ".-..";
    letra_a_morse['M'] = "--";
    letra_a_morse['N'] = "-.";
    letra_a_morse['O'] = "---";
    letra_a_morse['P'] = ".--.";
    letra_a_morse['Q'] = "--.-";
    letra_a_morse['R'] = ".-.";
    letra_a_morse['S'] = "...";
    letra_a_morse['T'] = "-";
    letra_a_morse['U'] = "..-";
    letra_a_morse['V'] = "...-";
    letra_a_morse['W'] = ".--";
    letra_a_morse['X'] = "-..-";
    letra_a_morse['Y'] = "-.--";
    letra_a_morse['Z'] = "--..";

    map<string, char> morse_a_letra;
    for (pair<char, string> p : letra_a_morse) {
        char letra = p.first;
        string codigo = p.second;
        morse_a_letra[codigo] = letra;
    }

    cout << "Traductor de código Morse" << endl;
    while (true) {
        cout << "> ";
        string entrada;
        getline(cin, entrada);

        if (EstaEnMorse(entrada)) {
            for (int i = 0; i < entrada.size(); i++) {
                if (entrada[i] == '.' || entrada[i] == '-') {
                    int j = i;
                    while (j < entrada.size() && (entrada[j] == '.' || entrada[j] == '-')) {
                        j++;
                    }
                    string codigo = entrada.substr(i, j - i);
                    cout << morse_a_letra[codigo];
                    i = j;
                }
            }
        } else {
            for (char c : entrada) {
                if (c == ' ') {
                    continue;
                }
                cout << letra_a_morse[c] << ' ';
            }
        }
        cout << endl;
    }
    return 0;
}