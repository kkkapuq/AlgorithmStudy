import java.lang.reflect.Array;
import java.util.Arrays;

public class Leetcode_122_Best_Time_to_Buy_and_Sell_Stock_II {
    public static int maxProfit(int[] prices) {
        int n = prices.length;
        int profit = 0;
        for(int i = 0; i < n-1; i++){
            int price = prices[i];
            if(price < prices[i+1]){
                profit += prices[i+1] - price;
            }
        }
        return profit;
    }

//    public static void main(String[] args) {
//        int temp = maxProfit(new int[]{7,1,5,3,6,4});
//        System.out.println(temp);
//    }

}
