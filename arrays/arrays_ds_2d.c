#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int calc_max_sum(int arr[6][6]){
  int max_sum = -1000;
  int i = 0;
  int j = 0;
  for(int arr_i = 0; arr_i < 4; arr_i++){
     for(int arr_j = 0; arr_j < 4; arr_j++){
         int sum = 0;
         sum += arr[arr_i][arr_j] + arr[arr_i][arr_j + 1] + arr[arr_i][arr_j + 2] + arr[arr_i + 1][arr_j + 1] + arr[arr_i + 2][arr_j] + arr[arr_i + 2][arr_j + 1] + arr[arr_i+2][arr_j + 2];
         if (sum > max_sum){
             max_sum = sum;
             i = arr_i;
             j = arr_j;
         }
     }
  }
  return max_sum;
}

int main(){
  int arr[6][6];
  int myPoints[6][6] = {
    {1, 8, 8, 8, 1, 1}, 
    {1, 1, 8, 1, 1, 1}, 
    {1, 8, 8, 8, 1, 1}, 
    {1, 1, 1, 9, 9, 9}, 
    {1, 1, 1, 1, 9, 1}, 
    {1, 1, 1, 9, 9, 9}
  };

  int max_sum = calc_max_sum(myPoints);

  printf("%d\n", max_sum == 9 * 7);
  return 0;
}
