import java.util.*;

public class Programmers_92334 {
    public static int[] solution(String[] id_list, String[] report, int k) {
        /*
        // 정답 return 해줄 배열 0으로 초기화
        int[] answer = new int[id_list.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = 0;
        }
        // 한 유저가 여러번 신고하는 것은 1번까지만 되므로 set을 이용해 중복을 제거한다.
        HashSet<String> hashSet = new HashSet<>(Arrays.asList(report));
        report = hashSet.toArray(new String[0]);

        // 신고자 : 신고횟수,
        // 메일수신자 : 수신횟수
        HashMap<String, Integer> reportMap = new LinkedHashMap<>();
        HashMap<String, Integer> mailedMap = new LinkedHashMap<>();

        // 신고자별로 신고당한 횟수와 신고여부 0으로 초기화.
        for (int i = 0; i < id_list.length; i++) {
            reportMap.put(id_list[i], 0);
            mailedMap.put(id_list[i], 0);
        }

        // 신고자별로 신고당한 횟수 넣어주는 작업
        for (int i = 0; i < report.length; i++) {
            String temp = report[i];
            String[] tempArray = temp.split(" ");
            //신고자와 피신고자 구분
            String reporter = tempArray[0];
            String reportee = tempArray[1];

            reportMap.put(reportee, reportMap.get(reportee) + 1);
        }

        for (int i = 0; i < id_list.length; i++) {
            if (reportMap.get(id_list[i]) > k) {
                for (int j = 0; j < report.length; j++) {
                    String temp = report[j];
                    String[] tempArray = temp.split(" ");
                    //신고자와 피신고자 구분
                    String reporter = tempArray[0];
                    String reportee = tempArray[1];

                    // i사용자를 신고한 모든 사람들의 mailedMap에 +1 해줘야됨.
                    if(reportee.equals(id_list[i])){
                        mailedMap.put(reporter, mailedMap.get(reporter) + 1);
                    }
                }
            }
        }


        // 메일 받는 횟수를 answer에 대입해주면 끝
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = mailedMap.get(id_list[i]);
        }

        return answer;

         */

        // @param idList : 이용자의 ID를 담은 배열.
        // @param report : 신고한 이용자와 신고당한 이용자의 정보를 담은 배열. ex) "a b",.. -> a가 b를 신고
        // @param k      : 신고 횟수에 따른 정지 기준 정수값.
        // @return answer : id_list에 담긴 id 순서대로 각 유저가 받은 신고 결과 메일 개수 배열.
        int[] answer = new int[id_list.length];
        HashMap<String, HashSet<String>> reporterInfoMap = new HashMap<>();
        HashMap<String, Integer> reportedCountInfoMap = new HashMap<>();
        HashSet<String> reportSet = new HashSet<>(Arrays.asList(report));

        for(String reportInfo : reportSet){
            String reporter = reportInfo.split(" ")[0];  // 신고 한 사람
            String reported = reportInfo.split(" ")[1];  // 신고 당한 사람
            reporterInfoMap.putIfAbsent(reporter, new HashSet<String>(){{
                add(reported);
            }});
            reporterInfoMap.get(reporter).add(reported);
            reportedCountInfoMap.put(reported, reportedCountInfoMap.getOrDefault(reported, 0)+1);
        }

        for (String reported : reportedCountInfoMap.keySet()){
            int reportedCount = reportedCountInfoMap.get(reported);
            if(reportedCount >= k){
                // 메일 발송 대상
                for(int i=0; i<id_list.length; i++){
                    if(reporterInfoMap.containsKey(id_list[i]) && reporterInfoMap.get(id_list[i]).contains(reported)) {
                        answer[i]++;
                    }
                }
            }
        }
        return answer;

    }

    public static void main(String[] args) {
        int[] temp = solution(new String[]{"muzi", "frodo", "apeach", "neo"}, new String[]{"muzi frodo", "apeach frodo", "frodo neo", "frodo neo", "frodo neo", "muzi neo", "apeach muzi"}, 2);
        System.out.println(temp);
    }


}
