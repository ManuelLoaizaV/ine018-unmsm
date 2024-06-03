#include <iostream>
using namespace std;

int ObtenerYardas(int pulgadas) {
    int yardas = pulgadas / 36;
    if (pulgadas % 36 > 0) {
        yardas++;
    }
    return yardas;
}

int ObtenerExcesoDeTela(int pulgadas) {
    return 36 * ObtenerYardas(pulgadas) - pulgadas;
}

void ReporteCompraDeTela(int pulgadas) {
    cout << "Necesitamos " << pulgadas << " pulgada(s)" << endl;
    cout << "Yardas a comprar: " <<  ObtenerYardas(pulgadas) << endl;
    cout << "Exceso de tela: " << ObtenerExcesoDeTela(pulgadas) << " pulgada(s)" << endl;
    cout << endl;
}

int main(void) {
    ReporteCompraDeTela(71);
    ReporteCompraDeTela(72);
    ReporteCompraDeTela(73);
    return 0;
}