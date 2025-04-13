#include <iostream>
#include <stack>
using namespace std;

string InvertirCadena(string s) {
	string r;
	for (int i = s.size() - 1; i >= 0; i--) {
		r += s[i];
	}
	return r;
}

string ConvertirABuena(string s) {
	stack<char> caracteres;
	for (int i = 0; i < s.size(); i++) {
		if (
			!caracteres.empty() &&
			islower(caracteres.top()) &&
			toupper(caracteres.top()) == s[i]
		) {
			caracteres.pop();
		} else {
			caracteres.push(s[i]);
		}
	}
	
	string r;
	while (!caracteres.empty()) {
		r += caracteres.top();
		caracteres.pop();
	}
	
	return InvertirCadena(r);
}

int main(void) {
	cout << ConvertirABuena("UNMSM") << endl;
	cout << ConvertirABuena("s") << endl;
	cout << ConvertirABuena("xabBAycCz") << endl;
	cout << ConvertirABuena("xaaabbbBBBAAAd") << endl;
	return 0;
}