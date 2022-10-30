import java.util.HashSet;
import java.util.Set;

public class Leetcode_128_Longest_Consecutive_Sequence {
    public static int longestConsecutive(int[] nums) {
        int answer = 0;
        if(nums == null || nums.length == 0) return 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!set.contains(nums[i] - 1)) {
                int templen = 0;
                while (set.contains(templen + nums[i])) {
                    templen++;
                }
                answer = Math.max(templen, answer);
            }
        }
        return answer;
    }

//    public static void main(String[] args) {
//        int temp = longestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1});
//        System.out.println(temp);
//    }
}
