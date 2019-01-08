import java.util.*;

public class GCD {
  private static int gcd_naive(int a, int b) {
    int current_gcd = 1;
    for(int d = 2; d <= a && d <= b; ++d) {
      if (a % d == 0 && b % d == 0) {
        if (d > current_gcd) {
          current_gcd = d;
        }
      }
    }

    return current_gcd;
  }

  private static int gcd_super_duper(int a, int b) {
    if (b == 0){
      return a;
    }
    int tmp = b;
    b = a % b;
    a = tmp;
//    System.out.println(a);
//    System.out.println(b);
//    System.out.println();
    return gcd_super_duper(a, b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();
    int first = gcd_naive(a, b);
    int second = gcd_super_duper(a, b);

    System.out.println(first == second);
    System.out.println(first);
    System.out.println(second);
  }
}
