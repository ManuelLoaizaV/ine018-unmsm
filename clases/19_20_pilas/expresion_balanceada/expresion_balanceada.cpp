#include <iostream>
#include <stack>
using namespace std;

bool EsApertura(char c) {
    return c == '{' || c == '[' || c == '(';
}

bool EsCerradura(char c) {
    return c == '}' || c == ']' || c == ')';
}

char ObtenerApertura(char c) {
    if (c == '}') {
        return '{';
    }
    if (c == ']') {
        return '[';
    }
    if (c == ')') {
        return '(';
    }
    return '\0';
}

bool EsBalanceada(string expresion) {
    stack<char> aperturas;
    int n = (int)expresion.size();
    for (int i = 0; i < n; i++) {
        if (EsApertura(expresion[i])) {
            aperturas.push(expresion[i]);
        } else if (EsCerradura(expresion[i])) {
            if (aperturas.empty() || aperturas.top() != ObtenerApertura(expresion[i])) {
                return false;
            }
            aperturas.pop();
        }
    }
    return aperturas.empty();
}

int main(void) {
    cout << EsBalanceada("()") << endl;
    cout << EsBalanceada(")(") << endl;
    cout << EsBalanceada("{[()]}") << endl;
    cout << EsBalanceada("{[(])}") << endl;
    cout << EsBalanceada("{{[[(())]]}}") << endl;
    cout << EsBalanceada("(([])") << endl;
    cout << EsBalanceada("{}()") << endl;
    cout << EsBalanceada("{(})") << endl;
    cout << EsBalanceada("{ s = 2 * (a[2] + 3); x = (1 + (2)); }") << endl;
    return 0;
}
