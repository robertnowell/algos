import java.util.*;

public class FibonacciPartialSum {
    private static long getFibonacciPartialSumNaive(long from, long to) {
        long sum = 0;

        long current = 0;
        long next  = 1;

        for (long i = 0; i <= to; ++i) {
            if (i >= from) {
                sum += current;
            }

            long new_current = next;
            next = next + current;
            current = new_current;
        }

        System.out.println("naive partial:");
        System.out.println(sum);
        return sum % 10;
    }

    private static long getFibonacciSum(long n){
        long a = 0, b = 1, c = a + b;
        for (int i = 2; i < n + 3; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c-1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();

        long fromsum = getFibonacciSum(from-1);
        long tosum  = getFibonacciSum(to);
        long partial = tosum - fromsum;
        System.out.println("from:");
        System.out.println(fromsum);
        System.out.println("to:");
        System.out.println(tosum);
        System.out.println("my partial:");
        System.out.println(partial);
        System.out.println("my partial last digit");
        System.out.println(partial%10);

        System.out.println("");
        long s = getFibonacciPartialSumNaive(from, to);
        System.out.println(s);

    }

}

