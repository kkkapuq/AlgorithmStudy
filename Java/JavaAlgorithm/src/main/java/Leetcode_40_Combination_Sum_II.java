import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Leetcode_40_Combination_Sum_II {

    public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        // 가능한 조합들을 넣어줄 comb
        List<Integer> comb = new ArrayList<>();
        // 결과값에 오름차순 정렬이니 한번해주기
        Arrays.sort(candidates);
        // 백트래킹 돌려주기
        dfs(candidates, target, 0, comb, answer);

        return answer;
    }
    public static void dfs(int[] can, int target, int start, List<Integer> comb, List<List<Integer>> answer){
        for(int i = start; i < can.length; i++){
            // 중복 제거
            if(i > start && can[i] == can[i-1]){
                continue;
            }
            // can[i] 가 target 수 그자체인 경우, 정답에 하나 넣어줌, 넘겨받은 comb로 초기화
            if(can[i] == target){
                List<Integer> tempComb = new ArrayList<>(comb);
                tempComb.add(can[i]);
                answer.add(tempComb);
            } else if (can[i] < target) { // 만약 target보다 작다면, 임의의 List에 값을 넣어주고 재귀 돌린다.
                List<Integer> tempComb = new ArrayList<>(comb);
                tempComb.add(can[i]);
                // target에서 현재 can[i] 값을 빼줘야, 다음에 can[i]가 target보다 작은지 판단하고
                // target보다 작은 수들만 조합을 이루도록 한다.
                dfs(can, target - can[i], i + 1, tempComb, answer);
            } else {
                break; // 만들수 없는 조합이면 아무것도 안함
            }
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> temp = combinationSum2(new int[]{10,1,2,7,6,1,5}, 8);
        System.out.println(temp);
    }
}
