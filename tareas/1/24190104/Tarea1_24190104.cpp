#include <iostream>
using namespace std;
int Multiplo(int n,int m) {
  int i;
  for(i=n;i<=n*m;i+=n){
    for(int j=1;j<m;j++){
      cout<<i<<",";
    }
    cout<<""<<i<<",";
  }
  cout<<endl;
  return i;
}
int main(){
  int n,m;
  cin>>n>>m;
  Multiplo(n,m);
  cout<<endl;
  return 0;
} 
