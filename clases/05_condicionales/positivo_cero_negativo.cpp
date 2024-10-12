#include <iostream>
using namespace std;

int main(void) {
	int n;
	cin >> n;

	if (n > 0) {
		cout << n << " es positivo" << endl;
	} else {
		// n <= 0
		if (n == 0) {
			cout << n << " es cero" << endl;
		} else {
			// n < 0
			cout << n << " es negativo" << endl;
		}
	}

	return 0;
}
