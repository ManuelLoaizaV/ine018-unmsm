#include <iostream>
#include <map>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	map<string, int> frecuencias;
	for (int i = 0; i < n; i++) {
		string nombre;
		cin >> nombre;
		if (!frecuencias.contains(nombre)) {
			cout << "OK" << endl;
			frecuencias[nombre] = 1;
		} else {
			cout << nombre << frecuencias[nombre] << endl;
			frecuencias[nombre]++;
		}
	}
	return 0;
}
