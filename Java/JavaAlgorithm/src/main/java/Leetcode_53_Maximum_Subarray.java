public class Leetcode_53_Maximum_Subarray {
    public static int maxSubArray(int[] nums) {
        /*int sum = nums[0];
        for(int i = 0; i < nums.length; i++){
            int tempSum = 0;
            for(int j = i; j < nums.length; j++){
                tempSum += nums[j];
                if(tempSum > sum) sum = tempSum;
            }
        }
        return sum;*/

        int n = nums.length;
        int max = Integer.MIN_VALUE, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            max = Math.max(sum, max);

            if(sum < 0) sum = 0;
        }
        return max;
    }

    public static void main(String[] args) {
        int temp = maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
        System.out.println(temp);
    }
}
