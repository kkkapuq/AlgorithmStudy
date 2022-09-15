import java.util.Arrays;

public class Leetcode_581_Shortest_Unsorted_Continuous_Subarray {
    public static int findUnsortedSubarray(int[] nums) {
        int answer = 0;
        int fisrtIndex = 0, lastIndex = 0;
        boolean flag = true;
        int[] sortedArray = nums.clone();
        //int[] sortedArray = nums 이렇게 하면 얕은복사가 일어나서 nums까지 정렬되버림
        Arrays.sort(sortedArray);

        if(Arrays.equals(nums, sortedArray)){
            return answer;
        }

        // nums = [2,6,4,8,10,9,15]
        // sortedArray = [2,4,6,8,9,10,15]
        for(int i = 0; i < sortedArray.length; i++){
            if(sortedArray[i] != nums[i]){
                if(flag){
                    flag = false;
                    fisrtIndex = i;
                }
                lastIndex = i;
            }
        }
        answer = lastIndex - fisrtIndex + 1;
        return answer;
    }

    public void dfs(){

    }

    public static void main(String[] args) {
        int temp = findUnsortedSubarray(new int[]{2,6,4,8,10,9,15});
        System.out.println(temp);
    }
}
