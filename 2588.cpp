#include <iostream>
using namespace std;

int main() {
	int a;
	string b;
	cin>>a>>b;
	cout<<a*(b[2]-48)<<'\n';
	cout<<a*(b[1]-48)<<'\n';
	cout<<a*(b[0]-48)<<'\n';
	cout<<a*(stoi(b))<<'\n';
	return 0;
}