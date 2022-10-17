import java.util.List;

public class Leetcode_35_Search_Insert_Position {
    public static int searchInsert(int[] nums, int target) {
//        if(nums[nums.length-1] < target){
//            return nums.length;
//        } else if(nums[0] > target){
//            return 0;
//        } else if(nums.length == 1 && nums[0] == target){
//            return 0;
//        }
//        if(nums.length == 2){
//            int first = nums[0];
//            int sec = nums[1];
//
//            if(target == first) return 0;
//            if(target == sec) return 1;
//            if(target > first && target < sec) return 1;
//        }
//        if(nums.length == 3){
//            int first = nums[0];
//            int sec = nums[1];
//            int third = nums[2];
//
//            if(target == first) return 0;
//            if(target == sec) return 1;
//            if(target == third) return 2;
//            if(target > first && target < sec) return 1;
//            if(target > sec && target < third) return 2;
//        }
//
//        if(nums.length > 3){
//            int left = 1, right = nums.length-2;
//            while(left < right){
//                if(nums[left] == target) return left;
//                if(nums[right] == target) return right;
//                if(nums[left-1] < target && nums[left] > target) return left;
//                if(nums[right+1] > target && nums[right] < target) return right;
//                if(nums[left] < target){
//                    left++;
//                } else if(nums[right] > target) {
//                    right--;
//                }
//            }
//        }
//        return nums.length;

        int left = 0, right = nums.length-1;
        while(left <= right){
            int mid = (left+right)/2;
            if(nums[mid] == target){
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }


    public static void main(String[] args) {
        int temp = searchInsert(new int[]{1,3,5}, 1);
        System.out.println(temp);
    }
}
