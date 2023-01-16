public class Leetcode_11_Container_With_Most_Water {
    public static int maxArea(int[] height) {
        // 투포인터 복습
        int l = 0;
        int r = height.length - 1;
        int maxAmount = Integer.MIN_VALUE;
        int tempHeight = 0;

        while (l < r) {
            if (height[l] < height[r]) {
                tempHeight = height[l];
                int amount = r - l;
                maxAmount = Math.max(amount * tempHeight, maxAmount);
                l++;
            } else {
                tempHeight = height[r];
                int amount = r - l;
                maxAmount = Math.max(amount * tempHeight, maxAmount);
                r--;
            }
        }
        return maxAmount;
    }

//    public static void main(String[] args) {
//        int temp = maxArea(new int[]{7,8,6,2,5,4,8,3,7});
//        System.out.println(temp);
//    }
}
