import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      int n = Integer.parseInt(br.readLine());
      int m = Integer.parseInt(br.readLine());
      
      String line = br.readLine();
      
      int [] dp = new int [m];
      
      for (int i = 0; i < m; i++) {
        if (line.charAt(i) == 'I') {
          dp[i] = 1;
          if (i - 2 >= 0 && line.charAt(i - 1) == 'O' && line.charAt(i - 2) == 'I') {
            dp[i] = dp[i - 2] + 1;
          }
        }
      }
      int cnt = 0;
      for (int i = 0; i < m; i++){
        // System.out.println(dp[i]);
        if (dp[i] > n) {
          cnt += 1;
        }
      }
      System.out.println(cnt);
  }
}