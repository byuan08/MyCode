#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double get_max_loot_value(const unsigned int &n, const unsigned long &W,
					      const vector<unsigned int> &v, const vector<unsigned int> &w) {

	static vector<double> unit_v(n);
	for (int i=0; i < v.size();i++) {

		unit_v[i] = v[i]/w[i];
	}
	
}

int main() {

	unsigned int n;
	unsigned long W;
	vector<unsigned int> v;
	vector<unsigned int> w;
	cin >> n >> W;
	for (int i=0;i<n;i++) 
		cin >> v[i] >> w[i];

	vector<double> unit_v(n);
	for (int i=o; i<v.size();i++)
		unit_v[i] = v[i]/w[i];



	double out = get_max_loot_value(n, W, v, w);

	cout.precision(5);
	cout << out << endl;
	return 0;


	




}

