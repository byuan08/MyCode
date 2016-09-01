#include <iostream>

using namespace std;
int* ct;

int get_change(int m) {
	
	if (m/10 > 0) {
		return m/10 + get_change(m%10);
	}
	else if (m/5 > 0) {
		
		return m/5 + get_change(m%5);
	}
	else {
		return m;

	}
}

int main() {

	int m;
	cin >> m;
	cout << get_change(m) << '\n';

}
