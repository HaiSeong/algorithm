import java.util.*;
import java.io.*;



public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      
      P [] persons = new P [n];
      
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        persons[i] = new P(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
      }
       
      int [] answer = new int [n];
      
      for (int i = 0; i < n; i++) {
        answer[i] += 1;
        for (int j = 0; j < n; j++) {
          if (persons[i].x < persons[j].x && persons[i].y < persons[j].y) {
            answer[i] += 1;
          }
        }
      }
      
      for (int i = 0; i < n; i++) {
        System.out.print(answer[i] + " ");
      }
  }
}

class P {
  int x;
  int y;
  
  public P (int x, int y) {
    this.x = x;
    this.y = y;
  }
}