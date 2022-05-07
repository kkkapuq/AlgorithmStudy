#include<iostream>
#include<vector>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, K;
	cin >> N >> K;
	vector<bool> arr(200001, false);
	queue<pair<int, int>> q;
	
	q.push({ N,0 });
	arr[N] = true;
	while (!q.empty()) {
		pair<int, int> p = q.front();
		q.pop();
		int pos = p.first;
		int turn = p.second;
		arr[pos] = true;
		if (pos == K) {
			cout << turn;
			return 0;
		}
		if (pos<=100000 && !arr[2 * pos]) {
			arr[2 * pos] = true;
			q.push({ 2 * pos,turn + 1 });
		}
		if (pos<=100000 && !arr[pos +1]) {
			arr[pos +1] = true;
			q.push({ pos + 1,turn + 1 });
		}
		if (pos!=0 && !arr[pos -1]) {
			arr[pos - 1] = true;
			q.push({ pos - 1,turn + 1 });
		}
	}
}
