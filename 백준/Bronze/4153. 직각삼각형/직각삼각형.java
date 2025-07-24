import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      
      while (true) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int a, b, c;
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        if (a == 0 && b == 0 && c == 0) {
          break;
        }
        
        String answer = "wrong";
        
        if (a * a == b * b + c * c) {
          answer = "right";
        }
        if (a * a + b * b == c * c) {
          answer = "right";
        }
        if (a * a + c * c == b * b) {
          answer = "right";
        }
        
        System.out.println(answer);
      }
  }
}