import java.util.*;
import java.io.*;

class Point {
  int x;
  int y;
  
  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int n = Integer.parseInt(br.readLine());
      Point [] points = new Point [n];
      
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        points[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
      }
      
      Arrays.sort(points, (p1, p2) -> {
        if (p1.x != p2.x) {
          return p1.x - p2.x;
        }
        return p1.y - p2.y;
      });
      
      for (int i = 0; i < n; i++) {
        bw.write(points[i].x + " " + points[i].y + "\n");
      }
      
      bw.flush();
      bw.close();
  }
}