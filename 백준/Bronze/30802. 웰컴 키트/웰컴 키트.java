import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      StringTokenizer st = new StringTokenizer(br.readLine());
      List<Integer> shirts = new ArrayList<>();
      for (int i = 0; i < 6; i++) {
        shirts.add(Integer.parseInt(st.nextToken()));
      }
      StringTokenizer st2 = new StringTokenizer(br.readLine());
      int t = Integer.parseInt(st2.nextToken());
      int p = Integer.parseInt(st2.nextToken());
      
      int answerT = 0;
      for (int i = 0; i < 6; i++) {
        answerT += ((shirts.get(i) + t - 1) / t);
      }
      int answerP = n / p;
      int answerP2 = n % p;
      
      System.out.println(answerT);
      System.out.println(answerP + " " + answerP2);
  }
}