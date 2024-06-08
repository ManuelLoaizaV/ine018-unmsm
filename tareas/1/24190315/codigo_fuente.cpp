#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    cout << "Programa TINKA, iniciemos..." << endl;

    vector<int> tinka(6);
    string jugada;
    cout << "Bolilla 1:" << endl;

    tinka[0] = rand()%45 + 1;
    jugada = to_string(tinka[0]);
    cout << jugada << endl;

    int i = 1;
    while (i <= 5){
        tinka[i] = rand()%45 + 1;
        int j = i - 1;
        while (j >= 0){
            if (tinka[i] == tinka[j]){
                j = -2;
            } else{
                j--;
            }
        }
        if (j == -1){
            cout << "Bolilla " << (i + 1) << ":" << endl;
            jugada += "-" + to_string(tinka[i]);
            cout << tinka[i] << endl;
            i++;
        }
    }
    cout << endl;
    cout << "La jugada es: " << jugada << endl;
    return 0;
}
