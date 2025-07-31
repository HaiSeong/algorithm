import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      int n = Integer.parseInt(br.readLine());
      int m = Integer.parseInt(br.readLine());
      
      StringBuilder finding_ = new StringBuilder("I");
      for (int i = 0; i < n; i++){
        finding_.append("OI");
      }
      String finding = finding_.toString();
      String line = br.readLine();
      
      int cnt = 0;
      
      for (int i = 0; i < m - finding.length() + 1; i++) {
        
        boolean same = true;
        for (int j = 0; j < finding.length(); j ++) {
          if (line.charAt(i + j) != finding.charAt(j)) {
            same = false;
            break;
          }
        }
        
        if (same) {
          cnt++;
        }
      }
      
      System.out.println(cnt);
  }
}