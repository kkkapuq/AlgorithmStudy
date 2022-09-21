public class Leetcode_42_Trapping_Rain_Water {
    public static int trap(int[] height) {
        int n = height.length;
        int answer = 0;

        //물을 가두려면 최소 3칸이 필요하므로, 이보다 적으면 0 리턴
        if (n < 3) {
            return 0;
        }
        // 물을 가둘 수 있는 왼쪽 높이와 오른쪽 높이를 나타내는 변수 선언
        int leftMax = 0, rightMax = height[n - 1];
        // 투포인터를 활용하기 위한 변수
        int left = 0, right = n - 2;

        //가둬진 물의 양을 알 수 있는 공식은..없고
        //현재 인덱스(i)가 leftMax보다 적으면, leftMax - height[i]가 현재 칸에 고여있는 물의 양이다.
        //따라서, 이걸 answer에 ++ 해주면 될듯?

        while (left <= right) {
            //만약 왼쪽 끝기둥이 오른쪽 끝기둥보다 크다면
            if (leftMax < rightMax) {
                //현재 기둥이 leftMax보다 클 경우 갱신해주기
                if (height[left] > leftMax) {
                    leftMax = height[left];
                } else {
                    answer += leftMax - height[left];
                }
                left++;
            } else {
                //오른쪽 끝기둥이 왼쪽 끝기둥보다 큰 경우
                //현재 기둥이 rightMax 보다 큰 경우 갱신
                if(height[right] > rightMax){
                    rightMax = height[right];
                } else {
                    answer += rightMax - height[right];
                }
                right--;
            }
        }
        return answer;
    }

//    public static void main(String[] args) {
//        int temp = trap(new int[]{2, 6, 4, 8, 10, 9, 15});
//        System.out.println(temp);
//    }
}
