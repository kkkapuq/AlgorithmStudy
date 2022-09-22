import java.util.ArrayList;
import java.util.List;

public class Leetcode_73_Set_Matrix_Zeroes {
    public static void setZeroes(int[][] matrix) {
        List<Integer> zeroIndex = new ArrayList<>();
        for(int i = 0; i < matrix.length; i++){
            boolean flag = false;
            for(int j = 0; j < matrix[i].length; j++){
                int temp = matrix[i][j];
                if(temp == 0){
                    zeroIndex.add(j);
                    flag = true;
                }
            }
            // 만약 배열 내 0이 존재한다면 해당 행을 모두 0으로 만든다.
            if(flag){
                matrix[i] = makeZero(matrix[i]);
            }
        }

        // 0이 있는 열을 모두 0으로 만들어주는 작업
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < zeroIndex.size(); j++){
                int index = zeroIndex.get(j);
                matrix[i][index] = 0;
            }
        }

        System.out.println(matrix);
    }

    public static int[] makeZero(int[] matrix){
        int []temp = matrix;
        for(int i = 0; i < matrix.length; i++){
            temp[i] = 0;
        }
        return temp;
    }

    public static void main(String[] args) {
        setZeroes(new int[][]{{0,1,2,0}, {3,4,5,2}, {1,3,1,5}});
    }
}
