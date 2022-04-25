#include<iostream>
#include<vector>

using namespace std;

int solution(int N,int S,vector<int> arr) {
	int p1=0;
	int p2 = 0;
	int sum = arr[0];

	int minLength = 0;
	while (p1 <= p2 && p2<N) {
		if (sum >= S) {
			int length = p2 - p1 + 1;
			if (minLength == 0 || length < minLength) minLength = length;
			sum -= arr[p1++];
		}
		else {
			if (p2 == N - 1) break;
			sum += arr[++p2];
		}
	}

	return minLength;

}

int main() {
	int N, S;
	cin >> N>>S;

	vector<int> vec(N);
	for (int i = 0; i < vec.size(); i++) {
		cin >> vec[i];
	}
	cout << solution(N, S, vec);

}