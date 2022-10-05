import java.util.Arrays;

public class Leetcode_55_Jump_Game {

    public static boolean canJump(int[] nums) {

        if(nums.length == 1)
            return true;

        // 인덱스별 최대값
        int maxIndex = Integer.MIN_VALUE;
        // 목표 인덱스 값
        int lastIndex = nums.length-1;

        for(int i = 0; i < nums.length; i++){
            maxIndex = Math.max(maxIndex, i + nums[i]);
            if(maxIndex <= i){
                return false;
            } else if(maxIndex >= lastIndex){
                return true;
            }
        }
        return false;
    }

//    public static void main(String[] args) {
//        boolean temp = canJump(new int[]{7,1,5,3,6,4});
//        System.out.println(temp);
//    }
}
