import java.util.*;
import java.io.*;

public class Main {
    static int [][] graph = new int [15][15];
    
    static int count(int k, int n) {
      if (k == 0) {
        return n;
      }
      
      if (graph[k][n] != 0) {
        return graph[k][n];
      }
      
      int cnt = 0;
      
      for (int i = 1; i <= n; i++) {
        cnt += count(k-1, i);
      }
      
      graph[k][n] = cnt;
      
      return cnt;
    }
  
  
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(br.readLine());
      
      for (int i = 0; i < t; i++) {
        int k = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        
        System.out.println(count(k, n));
      }
  }
}