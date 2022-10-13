import java.util.Stack;

public class Leetcode_20_Valid_Parentheses {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack();

        String[] list = s.split("");
        if (list[0].equals(")") || list[0].equals("}") || list[0].equals("]"))
            return false;

        for (int i = 0; i < list.length; i++) {
            if (list[i].equals("(") || list[i].equals("{") || list[i].equals("[")) {
                stack.push(list[i]);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    String temp = stack.peek();
                    switch (temp) {
                        case "(":
                            if (list[i].equals(")")) {
                                stack.pop();
                                continue;
                            } else {
                                return false;
                            }
                        case "{":
                            if (list[i].equals("}")) {
                                stack.pop();
                                continue;
                            } else {
                                return false;
                            }
                        case "[":
                            if (list[i].equals("]")) {
                                stack.pop();
                                continue;
                            } else {
                                return false;
                            }
                    }
                }
            }
        }
        if (stack.isEmpty()) {
            return true;
        }
        return false;
    }


}//    public static void main(String[] args) {
//        Leetcode_20_Valid_Parentheses temp = new Leetcode_20_Valid_Parentheses();
//        boolean t = temp.isValid("()[]{}");
//        System.out.println(t);
//    }
