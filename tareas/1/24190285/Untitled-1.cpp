#include <iostream>
#include <iostream>
using namespace std;
int main(){
  int x,y, potencia=0;
  do{
    cin>>x>>y;
    if(x>0){
      potencia=x^y;
    }
  }
  while(x>0&&y>0);
  

  cout<<potencia<<endl;
  
return 0;  
}