import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Leetcode_Generate_Parentheses {
    static List<String> output;
    static Deque<Character> stack;
    static StringBuilder sb;

//    public static void main(String[] args){
//        System.out.println(generateParenthesis(10));
//    }

    public static List<String> generateParenthesis(int n) {
        output = new ArrayList<>();
        stack = new ArrayDeque<>();
        sb = new StringBuilder();

        comb(0, 0, n);
        return output;
    }

    static void comb(int left, int right, int n){
        if(left == n && right == n){
            output.add(sb.toString());
            return;
        }

        if (left < n){
            stack.add('(');
            sb.append('(');
            comb(left + 1, right, n);
            stack.poll();
            sb.deleteCharAt(sb.length() - 1);
        }
        if(right < n){
            if(stack.size() > right){
                sb.append(')');
                comb(left, right+1, n);
                sb.deleteCharAt(sb.length()-1);
            }
        }
    }
}
