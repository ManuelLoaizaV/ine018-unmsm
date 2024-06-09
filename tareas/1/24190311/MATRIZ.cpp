#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    int A,B,C,D;
    cin >>A>>B>>C>>D;

    int DETERMINANTE=A*D-B*C;
    cout<<DETERMINANTE<<endl;
    return 0;
}
