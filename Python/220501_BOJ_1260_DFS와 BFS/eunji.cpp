#include<iostream>
#include<vector>
#include <queue>
#include<stack>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N, M, V;

	cin >> N >> M >> V;
	vector<vector<bool>> arr (N+1,vector<bool> (N+1,false));

	for (int i = 0; i < M; i++) {
		int from, to;
		cin >> from >> to;

		arr[from][to] = true;
		arr[to][from]=true;
	}
	
	//DFS
	stack <int> st;
	bool visit[1001] = { false, };
	st.push(V);
	int count = 0;

	while (!st.empty()) {
		int x=st.top();
		st.pop();
		if (visit[x]) {
			continue;
		}
		visit[x] = true;
		cout << x << " ";
		if (++count == N) break;
		for (int i = N; i >=1; i--) {
			if ((arr[x][i]) && (!visit[i])) {
				st.push(i);
			}
		}
	}
	cout << endl;

	//BFS
	queue<int> q;
	bool visit2[1001] = { false, };

	q.push(V);
	visit2[V] = true;
	count = 0;

	while (!q.empty()) {
		int p = q.front();
		q.pop();
		cout << p << " ";
		if (++count == N) break;
		for (int i = 1; i <= N; i++) {
			if (arr[p][i]&& !visit2[i]) {
				visit2[i] = true;
				q.push(i);
			}
		}
	}
}
