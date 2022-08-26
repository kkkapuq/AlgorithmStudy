public class Leetcode_785_Is_Graph_Bipartite {
    public static void main(String[] args){
    }

    public boolean isBipartite(int[][] graph) {
        int[] colors = new int[graph.length];

        //그래프 크기만큼 반복, 색칠되어있지 않다면 색칠해줌
        for(int i=0; i<graph.length; i++){
            if(colors[i] == 0 && !hasEvenCycle(graph, colors, i, 1))
                return false;
        }

        return true;
    }

    private boolean hasEvenCycle(int[][] g, int[] colors, int node, int c) {
        // 들어온 색(c)와 colors[node]가 동일하다면 true return
        if(colors[node] != 0){
            return colors[node] == c;
        }

        // 색칠해주기
        colors[node] = c;


        //인접한 모든 노드 탐색
        for(int n : g[node]){
            if(!hasEvenCycle(g, colors, n, -c))
                return false;
        }
        return true;
    }


}
