import java.util.*;
import java.io.*;



public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int n = Integer.parseInt(br.readLine());
      
      P [] persons = new P [n];
      
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int age = Integer.parseInt(st.nextToken());
        String name = st.nextToken();
        persons[i] = new P(age, name, i);
      }
      
      Arrays.sort(persons);
      
      for (var p : persons) {
        bw.write(String.format("%d %s\n", p.age, p.name));
      }
      bw.flush();
      bw.close();
  }
}

class P implements Comparable<P> {
  
  int age;
  String name;
  int order;
  
  public P (int age_, String name_, int order_) {
    age = age_;
    name = name_;
    order = order_;
  }
  
  public int compareTo(P other) {
    if (age != other.age) {
      return age - other.age;
    }
    return order - other.order;
  }
}