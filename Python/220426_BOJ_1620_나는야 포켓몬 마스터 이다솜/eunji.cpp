#include <map>
#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N, M;
	map<int, string> m1;
	map<string, int> m2;

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		string s;
		cin >> s;
		m1[i] = s;
		m2[s] = i;
	}
	for (int i = 1; i <= M; i++) {
		string s;
		cin >> s;
		if (s[0] >= 65) {
			cout << m2[s] << '\n';
		}
		else {
			cout << m1[stoi(s)]<< '\n';
		}
	}


}
