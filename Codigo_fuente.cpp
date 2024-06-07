#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
/*Esta funcion sirve para que la computadora al momento de elegir el valor me imprima en la salida el valor pero con el nombre
que asigne a cada opcion del juego*/
string Eleccion_de_computadora (int valor){
    if(valor == 1){
        return "Piedra";
    } else if(valor == 2){
        return "Papel";
    } else {
        return "Tijera";
    }
}
/*Esta funcion sirve para evaluar las jugadas entre la computadora y el jugador*/
void Evalua_juego(int n, int& ganadas_jugador, int& ganadas_computadora, int empates){
    srand(time(0));
    int valor = 1 + rand() % 3;//El numero que elige el computador
    if(valor == n){
        cout << "Empate" << endl;
        empates++;} //El aumento en el contador de empates servira mas adelante
        if(valor == n - 1 || valor == n + 2){
            cout << "Ganaste" << endl;
            ganadas_jugador++;}//El aumento en el contador de ganadas del jugador servira mas adelante
            if(valor == n + 1 || valor == n - 2){
                cout << "Perdiste" << endl;
                ganadas_computadora++;}//El aumento en el contador de ganadas del computador servira mas adelante
    cout << "La computadora jugo: " << Eleccion_de_computadora(valor) << endl;
}
int main(){
/*Mostramos los valores que se asignan a cada opcion del juego*/
cout << "Piedra = 1" << endl;
cout << "Papel  = 2" << endl;
cout << "Tijera = 3" << endl;
int casos;
cout << "Al mejor de: ";
cin >> casos;// Cuantas veces queremos jugar
//Iniciamos contadores
int empates = 0;
int ganadas_jugador = 0;
int ganadas_computadora = 0;
int casos_jugados = 0;
while(casos_jugados < casos) {//Para que se ejecute hasta que se complete los casos totales elegidos
        int n;
        cout << "Elige tu movimiento: ";
        cin >> n;
        if (n >= 1 && n <= 3) {
            Evalua_juego(n, ganadas_jugador, ganadas_computadora, empates);
            casos_jugados++;//Ponemos nuestros casos jugados
        } else {
            cout << "Elige un numero valido (1, 2 o 3)." << endl;//Por si elegimos un numero que no representa ninguna opcion
        }
    }
    //Estas condicionales sirven para mostrarnos dependiendo de la cantidad de ganadas, perdidas o empates quien gano definitivamente
    int k = (casos/2) + 1;
    if(ganadas_jugador == k || ganadas_jugador == casos) {
        cout << "Eres el ganador absoluto!!!!" << endl;
    } else if(ganadas_computadora == k || ganadas_computadora == casos) {
        cout << "La computadora te supero XD" << endl;
    } else if (empates == k || ganadas_computadora == casos) {
        cout << "Empate definitivo" << endl;
    } else {
        cout << "Vuelve a intentarlo, no hay un ganador definitivo" << endl;
    }
    return 0;
}
