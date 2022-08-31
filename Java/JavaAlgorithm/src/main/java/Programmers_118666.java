import java.util.HashMap;

public class Programmers_118666 {
    public static String solution(String[] survey, int[] choices) {
        StringBuilder sb = new StringBuilder();
        HashMap<String, Integer> characterMap = new HashMap<>();
        //1번지표
        characterMap.put("R", 0);
        characterMap.put("T", 0);
        //2번지표
        characterMap.put("C", 0);
        characterMap.put("F", 0);
        //3번지표
        characterMap.put("J", 0);
        characterMap.put("M", 0);
        //4번지표
        characterMap.put("A", 0);
        characterMap.put("N", 0);

        // 점수 부여
        for (int i = 0; i < survey.length; i++) {
            String[] temp = survey[i].split("");
            String first = temp[0];
            String second = temp[1];

            switch (choices[i]) {
                case 1:
                    characterMap.put(first, characterMap.get(first) + 3);
                    continue;
                case 2:
                    characterMap.put(first, characterMap.get(first) + 2);
                    continue;
                case 3:
                    characterMap.put(first, characterMap.get(first) + 1);
                    continue;
                case 5:
                    characterMap.put(second, characterMap.get(second) + 1);
                    continue;
                case 6:
                    characterMap.put(second, characterMap.get(second) + 2);
                    continue;
                case 7:
                    characterMap.put(second, characterMap.get(second) + 3);
                    continue;
            }
        }

        //정리된 값을 토대로 1~4번 지표를 기반으로한 성격유형 만들어주기
        //1번지표
        if(characterMap.get("R") > characterMap.get("T")){
            sb.append("R");
        } else if(characterMap.get("R") < characterMap.get("T")){
            sb.append("T");
        } else {
            sb.append("R");
        }

        //2번지표
        if(characterMap.get("C") > characterMap.get("F")){
            sb.append("C");
        } else if(characterMap.get("C") < characterMap.get("F")){
            sb.append("F");
        } else {
            sb.append("C");
        }

        //3번지표
        if(characterMap.get("J") > characterMap.get("M")){
            sb.append("J");
        } else if(characterMap.get("J") < characterMap.get("M")){
            sb.append("M");
        } else {
            sb.append("J");
        }

        //4번지표
        if(characterMap.get("A") > characterMap.get("N")){
            sb.append("A");
        } else if(characterMap.get("A") < characterMap.get("N")){
            sb.append("N");
        } else {
            sb.append("A");
        }

        String answer = sb.toString();
        return answer;
    }

//    public static void main(String[] args) {
//        String temp = solution(new String[]{"AN", "CF", "MJ", "RT", "NA"}, new int[]{5, 3, 2, 7, 5});
//        System.out.println(temp);
//    }
}
