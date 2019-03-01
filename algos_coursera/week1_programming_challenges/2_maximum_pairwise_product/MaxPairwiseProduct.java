import java.util.*;
import java.io.*;
import java.lang.Math.*;

public class MaxPairwiseProduct {
    static int getMaxPairwiseProduct(int[] numbers) {
        int max_ind_1 = 0;
        int max_ind_2 = 0;
        int n = numbers.length;

        for (int i = 0; i < n; ++i) {
            if (numbers[i] > numbers[max_ind_1]) {
              if (numbers[max_ind_1] > numbers[max_ind_2]) {
                max_ind_2 = max_ind_1;
              }
              max_ind_1 = i;
            }
            else if (numbers[i] > numbers[max_ind_2]) {
                max_ind_2 = i;
            }
        }

        return numbers[max_ind_1] * numbers[max_ind_2];
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
        System.out.println(getMaxPairwiseProduct(numbers));
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}