import java.util.HashMap;

public class Leetcode_169_Majority_Element {
     public static int majorityElement(int[] nums) {
        // 해시맵, 길이, 비교군 m, 정답
        HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer>();
        int n = nums.length;
        int m = n / 2;


        for(int i = 0; i < n; i++){
            if(numMap.containsKey(nums[i])){
                int temp = numMap.get(nums[i]) + 1;
                numMap.put(nums[i], temp);
            } else {
                numMap.put(nums[i], 1);
            }
        }

        for(int i : numMap.keySet()){
            if(numMap.get(i) > m){
                return i;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int temp = majorityElement(new int[]{3, 2, 3});
        System.out.println(temp);
    }
}
