#include<iostream>
using namespace std;

int divisores(int n){
	for(int i= 1; i<n; i++){
		if(n%i==0){
			cout<<i<<" ";
		}
	}
    return n;
}
int main(void){
	
    int a;
    cin>>a;
    int acu=0;
    for(int i =1; i<a; i++){
        if(a%i==0){    	
            acu+=i;} 
	 } 
	 cout<<"Los divisores de "<< a<< " son: "<<divisores(a)<<endl;
	 cout<<"La suma de divisores del numero "<< a <<" sin contar a " << a<< " son: "<<acu<<endl; 
	 
	 if(acu==a){
	 	cout<<"El numero es perfecto"<<endl;}   
	 else{
	 	cout<<"No es perfecto"<<endl;}

     return 0;
}