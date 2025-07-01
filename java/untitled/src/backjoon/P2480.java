package backjoon;

import java.util.Scanner;

public class P2480 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a, b, c;
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();

        int answer;
        if (a == b && b == c) {
            answer = 10000 + a * 1000;
        }
        else if (a != b && b != c && a != c) {
            answer = Math.max(c, (Math.max(a, b))) * 100;
        }
        else {
            if (a == b || a == c){
                answer = 1000 + a * 100;
            } else {
                answer = 1000 + b * 100;
            }
        }
        System.out.println(answer);
    }
}
