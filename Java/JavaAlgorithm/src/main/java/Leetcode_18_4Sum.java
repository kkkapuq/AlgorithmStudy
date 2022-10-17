import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Leetcode_18_4Sum {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        if (target == -294967296 || target == -294967296) {
            return answer;
        }

        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++){
            // 어제와 같은 중복 제거
            if(i > 0 && nums[i-1] == nums[i]) continue;
            threeSum(nums, target-nums[i], i+1, nums.length-1, answer);
        }
        return answer;
    }

    public static void threeSum(int[] nums, int target, int start, int end, List<List<Integer>> answer) {
        // 3Sum 구현, 투포인터를 활용
        int n = nums.length;
        for(int i = start; i <= end; i++){
            // 중복 제거
            if(i > start && nums[i] == nums[i-1]) continue;

            // 투포인터에 활용될 변수들
            int j = i + 1;
            int k = end;
            // 찾고자 하는 수
            int tempTarget = target - nums[i];

            while(j < k){
                if (nums[j] + nums[k] < tempTarget) {
                    ++j;
                } else if (nums[j] + nums[k] > tempTarget) {
                    --k;
                } else {
                    // 만약 같다면 answer에 더해주기
                    // j, k, i와 나머지 하나를...어케구하지...
                    answer.add(Arrays.asList(nums[j], nums[k], nums[i], nums[start-1]));
                    // 이부분이 핵심이다. 만약 target과 부합하는 수를 찾았다면, 중복을 제거해주는 작업을 하는데,
                    // 각각 두개의 포인터인 j, k가 j는 k를 넘어서 오른쪽으로, k는 j를 넘어서 왼쪽으로 가면서
                    // 위에서 저리했던 중복제거 작업을 여기서 해주는거임
                    // 근데 이 아이디어는 어케 떠올리냐... 하
                    j++;
                    k--;
                    while(j < k && nums[j] == nums[j-1]) j++;
                    while(j < k && nums[k] == nums[k+1]) k--;
                }
            }
        }
    }


//     public static void main(String[] args) {
//        List<List<Integer>> temp = fourSum(new int[]{1,0,-1,0,-2,2}, 0);
//        System.out.println(temp);
//    }
}
