import java.util.HashMap;
import java.util.Map;

public class Programmers_120956 {
    /**
     * 문제 : 옹알이(1)
     * 레벨 : 0
     * 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=java
     *
     * @param args
     */

    public static int solution(String[] babbling) {
        int answer = 0;
        Map<String, Boolean> map = new HashMap<>();
        map.put("aya", true);
        map.put("ye", true);
        map.put("woo", true);
        map.put("ma", true);

        for (String i : babbling) {
            i = i.replace("aya", "1");
            i = i.replace("ye", "1");
            i = i.replace("woo", "1");
            i = i.replace("ma", "1");
            i = i.replace("1", "");
            if(i.length() == 0){
                answer++;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        int temp = solution(new String[]{"aya", "yee", "u", "maa", "wyeoo"});
        System.out.println(temp);
    }
}
