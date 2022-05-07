#include<iostream>
#include<vector>
#include<queue>

#define INF 987654321

using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int V, E,K;
	cin >> V >> E;
	cin >> K;
	int D[20001];
	vector<pair<int,int>> adj[20001];

	for (int i = 0; i < E; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		adj[u].push_back({ v,w });
	}
	for (int i = 1; i <= V; i++) {
		D[i] = INF;
	}

	priority_queue<pair<int, int>> pq;
	pq.push({ 0,K });
	D[K] = 0;

	while (!pq.empty()) {
		int cost=-pq.top().first;
		int now = pq.top().second;
		pq.pop();
		for (int i = 0; i < adj[now].size(); i++) {
			int next=adj[now][i].first;
			int nextCost = adj[now][i].second;

			if (D[next] > cost + nextCost) {
				D[next] = cost + nextCost;
				pq.push({ -D[next],next });
			}
		}
	}
	
	for (int i = 1; i <= V; i++) {
		if (D[i] >= INF) cout << "INF" << endl;
		else cout << D[i] << endl;
	}
}
