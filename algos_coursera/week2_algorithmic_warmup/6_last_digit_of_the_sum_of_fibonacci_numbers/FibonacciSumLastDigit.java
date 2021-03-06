import java.util.*;

public class FibonacciSumLastDigit {
    private static long getFibonacciHugeNaive(long n, long m) {
        if (n <= 1)
            return n;

        long previous = 0;
        long current  = 1;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = tmp_previous + current;
        }

        return current % m;
    }

    private static long getFibonacci(long n) {
        if (n <= 1)
            return n;

        long previous = 0;
        long current  = 1;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = tmp_previous + current;
        }

        return current;
    }

    private static long get_pisano_period(long m) {
        long a = 0;
        long b = 1;
        long c = a + b;
        for (int i = 0; i < m * m; i++) {
            c = (a + b) % m;
            a = b;
            b = c;
            if (a == 0 && b == 1) {
                return i + 1;
            }
        }
        return 0;
    }

    private static long try_pisano_test(long m) {
        long a = 0;
        long b = 1;
        long c = a + b;
        for (int i = 0; i < m*m; i++){
            c = (a + b) % m;
            a = b;
            b = c;
            if (a == 0 && b == 1){
                return i + 1;
            }
        }
        return 0;
    }

    private static long getNthFibonacciModM(long n, long m){
        return getFibonacci((n % get_pisano_period(m))) % m;
    }

    private static long getFibonacciSumNaive(long n) {
        if (n <= 1)
            return n;

        long previous = 0;
        long current  = 1;
        long sum      = 1;

        for (long i = 0; i < n - 1; ++i) {
            long tmp_previous = previous;
            previous = current;
            current = tmp_previous + current;
            sum += current;
        }

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
        long n = scanner.nextLong();
        long s = getFibonacciSumNaive(n);

        long mine = getFibonacciSum(n);
        System.out.println(mine % 10);
        System.out.println(s);
    }

//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long n = scanner.nextLong();
//        long m = scanner.nextLong();
//        long naive = getFibonacciHugeNaive(n, m);
//        long sophisticated = getNthFibonacciModM(n, m);
//        System.out.println(naive);
//        System.out.println(sophisticated);
//        System.out.println(naive == sophisticated);
//    }
}