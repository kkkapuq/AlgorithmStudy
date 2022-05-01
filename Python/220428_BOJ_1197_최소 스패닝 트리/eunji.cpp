#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
vector<int> parent;

int getRoot(int p) {
	if (parent[p] == p) return p;
	else return (parent[p] = getRoot(parent[p]));
}

void unionParent(int a, int b) {
	a = getRoot(a);
	b = getRoot(b);
	if (a > b)parent[a] = b;
	else parent[b] = a;
}

bool isCycle(int a,int b) {
	a = getRoot(a);
	b = getRoot(b);
	if (a == b) return true;
	else return false;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin.tie(NULL);
	int result = 0;

	int V, E;
	cin >> V >> E;
	for (int i = 0; i <= V; i++) {
		parent.push_back(i);
	}

	// 크루스칼
	vector <pair<int, pair<int, int>>> edges;
	for (int i = 0; i < E; i++) {
		int X, Y, cost;
			cin >> X >> Y >> cost;
			edges.push_back({ cost,{X,Y} });
	}
	sort(edges.begin(), edges.end());

	for (int i = 0; i < edges.size(); i++) {
		if (!isCycle(edges[i].second.first, edges[i].second.second)) {
			result += edges[i].first;
			unionParent(edges[i].second.first, edges[i].second.second);
		}
	}

	cout << result;
}
