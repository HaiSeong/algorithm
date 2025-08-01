import java.util.*;
import java.io.*;

public class Main {
  
    private static long count(long [] trees, long cut) {
      long cnt = 0;
      for (var tree : trees) {
        if (tree > cut)
        cnt += (tree - cut);
      }
      return cnt;
    }
  
    public static void main(String[] args) throws Exception {
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      st = new StringTokenizer(br.readLine());
      long [] trees = new long [n];
      for (int i = 0; i < n; i++) {
        trees[i] = Integer.parseInt(st.nextToken());
      }
      
      long cur = 0;
      long step = 2000000001;
      while (step > 0) {
        while (count(trees, cur + step) >= m) {
          cur += step;
        }
        step /= 2;
      }
      
      System.out.println(cur);
  }
}