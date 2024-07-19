#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

int main(void) {
	string entradas;
	cin >> entradas;
	stack<char> buffer;
	for (char entrada : entradas) {
		if (entrada == 'B') {
			if (!buffer.empty()) {
				buffer.pop();
			}
		} else {
			buffer.push(entrada);
		}
	}

	string texto;
	while (!buffer.empty()) {
		texto += buffer.top();
		buffer.pop();
	}
	
	reverse(texto.begin(), texto.end());

	cout << texto << endl;
	return 0;
}
