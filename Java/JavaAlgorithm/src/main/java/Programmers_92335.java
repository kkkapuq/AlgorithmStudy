public class Programmers_92335 {
    public static int solution(int n, int k) {
        // k 진수로 변환한 str을 array로 변환
        String str = Integer.toString(n, k);
        StringBuilder sb = new StringBuilder();
        String temp = "";
        int answer = 0;

        int j = 0;
        for(int i = 0; i < str.length()-1 ; i = j){
            for(j = i + 1; j < str.length() && str.charAt(j) != '0'; j++);
            if(isPrimeNumber(Long.parseLong(str.substring(i, j))))
                answer++;
        }
        return answer;
    }

    public static boolean isPrimeNumber(Long x) {
        if (x <= 1) return false;

        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
//    public static void main(String[] args) {
//        int temp = solution(437674, 3);
//        System.out.println(temp);
//    }
}
