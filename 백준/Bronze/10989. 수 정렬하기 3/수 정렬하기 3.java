import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      
      int n = Integer.parseInt(br.readLine());
      // List<Integer> lst = new ArrayList<>();
      int[] lst = new int [n];
      for (int i = 0; i < n; i++) {
        lst[i] = Integer.parseInt(br.readLine());
        // lst.add(Integer.parseInt(br.readLine()));
      }
      
      Arrays.sort(lst);
      
      for (var num : lst) {
        bw.write(String.valueOf(num));
        bw.newLine();
      }
      
      bw.flush();
      bw.close();
  }
}
