import java.util.*;
import java.io.*;

public class Main {
  
  
    public static void main(String[] args) throws Exception {
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      
      Set<String> dd = new HashSet<>();
      
      for(int i = 0; i < n; i++) {
        dd.add(br.readLine());
      }
      
      List<String> answer = new ArrayList<>();
      
      for(int i = 0; i < m; i++) {
        String b = br.readLine();
        if (dd.contains(b)) {
          answer.add(b);
        }
      }
      
      Collections.sort(answer);
      
      bw.write(answer.size() + "\n");
      
      for (var a : answer) {
        bw.write(a);
        bw.newLine();
      }
      bw.flush();
      bw.close();
  }
}