#include <iostream>
using namespace std;

int main(void) {
    int n;
    cin>>n;
    cout << "La cuenta regresiva es ";
    for(int i=n; i > 0; i--) {
        cout<<i<<", ";
    }
    cout<<endl;
    return 0;
}


