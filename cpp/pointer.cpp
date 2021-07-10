#include <iostream>
using namespace std;


void printFcn(int *x_ptr);


int main(){
	int x[]={1,5,4,6,8,7};
	printFcn(x);
	return 0;
}


void printFcn(int *x_ptr){
	
	for(int i=0;i<6;++i){
           cout <<*(x_ptr+i)<< endl;
        }
}
