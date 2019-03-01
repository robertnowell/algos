import java.util.*;

public class FibonacciSumSquares {
    private static long getFibonacciSumSquaresNaive(long n) {
        if (n <= 1)
            return n;

        long previous = 0;
        long current  = 1;
        long sum      = 1;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = tmp_previous + current;
            sum += current * current;
        }

        System.out.println("naive sum:");
        System.out.println(sum);
        return sum % 10;
    }

    private static long getFib(long n) {
        if (n <= 1)
            return n;

        int previous = 0;
        int current  = 1;

        for (int i = 0; i < n - 1; ++i) {
            int tmp_previous = previous;
            previous = current;
            current = (tmp_previous + current);
        }

        return current;
    }

    private static long getQuickSumSquares(long n) {
        return getFib(n) * getFib(n+1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();

        System.out.println("fib23");
        System.out.println(getFib(23));

        long quick_sum = getQuickSumSquares(n);
        System.out.println("quick sum:");
        System.out.println(quick_sum);
        System.out.println("quick final digit");
        System.out.println(quick_sum % 10);

        long s = getFibonacciSumSquaresNaive(n);
        System.out.println("naive final digit:");
        System.out.println(s);
    }
}

