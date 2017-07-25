#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int binary_search(int *arr, int low, int high, int search){
  if (low > high){
    return -1;
  }
  int mid = (low + high)/2;
  // printf("low: %d\nhigh: %d\nmid: %d\narr[mid]: %d\nsearch: %d\n\n\n", low, high, mid, arr[mid], search);
  if (arr[mid] == search){
    return mid;
  }
  if (arr[mid] > search){
    return binary_search(arr, low, mid-1, search);
  }
  else{
    return binary_search(arr, mid+1, high, search);
  }
}

int main(void){
  int array[5] = {1, 3, 5, 7, 9};

  int test_0 = binary_search(array, 0, 4, 1);
  printf("%d\n", test_0 == 0);

  int test_1 = binary_search(array, 0, 4, 3);
  printf("%d\n", test_1 == 1);

  int test_2 = binary_search(array, 0, 4, 5);
  printf("%d\n", test_2 == 2);

  int test_3 = binary_search(array, 0, 4, 7);
  printf("%d\n", test_3 == 3);

  int test_4 = binary_search(array, 0, 4, 9);
  printf("%d\n", test_4 == 4);

  int test_5 = binary_search(array, 0, 4, 0);
  printf("%d\n", test_5 == -1);

  int test_6 = binary_search(array, 0, 4, -1);
  printf("%d\n", test_6 == -1);

  return 0;
}