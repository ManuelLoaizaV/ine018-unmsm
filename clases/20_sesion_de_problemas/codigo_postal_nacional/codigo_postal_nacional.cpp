#include <cctype>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;

bool EsNumerica(string s) {
    for (char c : s) {
        if (!isdigit(c)) {
            return false;
        }
    }
    return true;
}

int main(void) {
    map<string, vector<int>> codigos_postales;
    codigos_postales["Breña"] = {15082, 15083};
    codigos_postales["Magdalena del Mar"] = {7021, 15076, 15086};
    codigos_postales["San Miguel"] = {15086, 15087, 15088};
    codigos_postales["Pueblo Libre"] = {15083, 15084, 15086, 15088};
    codigos_postales["Jesus María"] = {2002, 15072, 15073, 15076, 15084};
    codigos_postales["Lima"] = {07006, 15001, 15003, 15004, 15006, 15018, 15046, 15079, 15081, 15082, 15083, 15085, 15088, 15093, 15101, 15822, 21001};

    map<int, vector<string>> distritos;
    for (pair<string, vector<int>> p : codigos_postales) {
        string distrito = p.first;
        vector<int> codigos_postales_del_distrito = p.second;
        for (int codigo : codigos_postales_del_distrito) {
            if (distritos.contains(codigo)) {
                distritos[codigo].push_back(distrito);
            } else {
                distritos[codigo] = {distrito};
            }
        }
    }

    while (true) {
        cout << "> ";
        string entrada;
        getline(cin, entrada);
        if (EsNumerica(entrada)) {
            int codigo = stoi(entrada);
            if (distritos.contains(codigo)) {
                for (string distrito : distritos[codigo]) {
                    cout << distrito << endl;
                }
            } else {
                cout << "El código postal no existe." << endl;
            }
        } else {
            if (codigos_postales.contains(entrada)) {
                for (int codigo : codigos_postales[entrada]) {
                    cout << codigo << endl;
                }
            } else {
                cout << "El distrito no existe." << endl;
            }
        }
    }
    return 0;
}