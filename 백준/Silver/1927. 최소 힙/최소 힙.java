import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
      
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int n = Integer.parseInt(br.readLine());
      
      PriorityQueue<Integer> queue = new PriorityQueue<>();
      
      for (int i = 0; i< n; i++) {
        int num = Integer.parseInt(br.readLine());
        if (num == 0) {
          if (queue.isEmpty()) {
            bw.write("0\n");
          } else {
            bw.write(queue.poll() + "\n");
          }
        }
        else {
          queue.add(num);
        }
      }
      bw.flush();
      bw.close();
  }
}