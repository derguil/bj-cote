#include <iostream>
using namespace std;

int main() {
	int a, y;
	cin >> a;

	if(!(a % 4)){
    y=1;
    if(!(a % 100)){
      y=0;
    }
		if(!(a % 400)){
      y = 1;
    }
  }
	
	if(y){
		cout << 1;
	} else {
		cout << 0;
	}
	return 0;
}