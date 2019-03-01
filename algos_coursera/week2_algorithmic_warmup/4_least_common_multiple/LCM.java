import java.util.*;

public class LCM {
  private static long lcm_naive(int a, int b) {
    for (long l = 1; l <= (long) a * b; ++l)
      if (l % a == 0 && l % b == 0)
        return l;

    return (long) a * b;
  }

  private static long lcm_super_duper(int a, int b) {
    if (a == 0 && b == 0){
      return 0;
    }
    long aa = (long)a;
    long bb = (long)b;

    return (aa*bb)/gcd_super_duper(aa,bb);
  }

  private static long gcd_super_duper(long a, long b) {
    if (b == 0){
      return (long) a;
    }
    long tmp = b;
    b = a % b;
    a = tmp;
    return gcd_super_duper(a, b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();
    long naive = lcm_naive(a, b);
    long super_duper = lcm_super_duper(a, b);
    System.out.println(naive == super_duper);
    System.out.println(naive);
    System.out.println(super_duper);
  }
}
