package backjoon;

import java.util.Scanner;

public class P2525 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        a += (b + c) / 60;
        a %= 24;
        b = (b + c) % 60;

        System.out.println(a + " " + b);
    }
}
