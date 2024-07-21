#include <iostream>
#include <set>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	set<string> nombres;
	for (int i = 0; i < n; i++) {
		string nombre;
		cin >> nombre;
		if (nombres.contains(nombre)) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
			nombres.insert(nombre);
		}
	}
	return 0;
}
