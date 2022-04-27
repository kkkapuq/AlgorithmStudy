#include<iostream>
#include<vector>
using namespace std;
int C;
vector<int> arr;
int countMod(int A, int d) {
	if (arr[d] != -1) {
		return arr[d];
	}
	int temp = d / 2;
	int result = countMod(A, temp) * countMod(A, d - temp);
	arr[d] = result % C;
	return arr[d];
}

int main() {
	int A, B;
	cin >> A >> B >> C;
	arr = vector<int>(B,-1);
	arr[1] = A % C;

	int temp = B / 2;
	int result = countMod(A, temp) * countMod(A,B-temp);
	
	cout << result%C;		
}
