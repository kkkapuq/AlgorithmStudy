import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Leetcode_31_Next_Permutation {
    static List<int[]> answerList = new ArrayList<>();

//    public static void main(String[] args) {
//        nextPermutation(new int[]{1, 2, 3});
//        System.out.println(answerList);
//    }

    public void nextPermutation(int[] num) {
      int dest = num.length - 2;
      for (; 0 <= dest && num[dest] >= num[dest + 1]; --dest);

      if (0 <= dest) {
        int target = num.length - 1;
        for (; num[dest] >= num[target]; --target);

        int tmp = num[dest];
        num[dest] = num[target];
        num[target] = tmp;
      }

      for (int end = num.length - 1; dest + 1 < end; ) {
        int tmp = num[++dest];
        num[dest] = num[end];
        num[end--] = tmp;
      }
    }

    // 순서를 지키면서 n 개중에서 r 개를 뽑는 경우
    // 사용 예시: perm(arr, output, visited, 0, n, 3);
    static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            answerList.add(output);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] != true) {
                visited[i] = true;
                output[depth] = arr[i];
                perm(arr, output, visited, depth + 1, n, r);
                output[depth] = 0; // 이 줄은 없어도 됨
                visited[i] = false;
            }
        }
    }
}
