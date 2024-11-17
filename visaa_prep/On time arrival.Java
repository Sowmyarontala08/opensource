import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        for(int i=0;i<a;i++) {
            int b=sc.nextInt();
            if(b>=30) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
    }
}
