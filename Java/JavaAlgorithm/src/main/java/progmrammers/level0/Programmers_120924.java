package progmrammers.level0;

public class Programmers_120924 {
    public static int solution(int[] common) {
        int answer = 0;
        int n = common.length;
        // 0이면 등차, 1이면 등비
        int flag = 0;

        // 공차
        int temp = common[1] - common[0];

        // common은 최소 3이상
        for (int i = 1; i < common.length - 1; i++) {
            if (common[i + 1] == common[i] + temp) {
                flag = 0;
            } else {
                // 등비수열이면 temp는 공비로 바뀜, 등비수열인거 알았으니까 break
                temp = common[i] / common[i - 1];
                flag = 1;
                break;
            }
        }

        if (flag == 0) {
            answer = common[n - 1] + temp;
        } else {
            answer = common[n - 1] * temp;
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1,2,3,4}));
    }
}
