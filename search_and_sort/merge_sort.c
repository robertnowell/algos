#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>

char * merge(char *s1, char *s2, char *s){
  // copy s1 and s2 into s one character at a time, selecting the smaller of each string
  // works because s1 and s2 are sorted
  int i = 0;
  int j = 0;
  int k = 0;
  while (s1[i] && s2[j]){
    if (s1[i] < s2[j]){
      s[k] = s1[i];
      i++;
    }
    else {
      s[k] = s2[j];
      j++;
    }
    k++;
  }

  // handle uneven length s1 and s2
  while (s1[i]){
    s[k] = s1[i];
    i++;
    k++;
  }
  while (s2[j]){
    s[k] = s2[j];
    j++;
    k++;
  }
  
  return s;
}

char *merge_sort(char *s){
  // stopping condition
  if (strlen(s) <= 1){
    return s;
  }

  // create substrings which split s in half
  int mid = (strlen(s))/2;
  int i = 0;
  char *sub1 = (char *)malloc(sizeof(char) * strlen(s));
  char *sub2 = (char *)malloc(sizeof(char) * strlen(s));
  while (i < mid){
    sub1[i] = s[i];
    i++;
  }
  sub1[i] = '\0';
  int j = 0;
  while (s[i]){
    sub2[j] = s[i];
    i++;
    j++;
  }
  sub2[j] = '\0';

  // debugging statement helpful for visualizing the stack trace during recursion
  // printf("s: %s\nmid: %d\nsub1: %s\nsub2: %s\n\n\n\n", s, mid, sub1, sub2);

  // merge results of recursive calls on substrings
  return merge(merge_sort(sub1), merge_sort(sub2), s);
}

int main(void){
  // create a string with alphabet in reverse
  char *alpha = (char *)malloc(sizeof(char) * 100);
  int i = 25;
  int j = 0;
  while (i > -1){
    alpha[j] = 'a' + i;
    j++;
    i--;
  }
  alpha[j] = '\0';
  printf("%d\n", strcmp(alpha, "zyxwvutsrqponmlkjihgfedcba") == 0);
  // sort
  alpha = merge_sort(alpha);
  // verify
  printf("%d\n", strcmp(alpha, "abcdefghijklmnopqrstuvwxyz") == 0);

  // create reverse number string 9 to 0
  char *num_str = (char *)malloc(sizeof(char) * 10);
  j = 9;
  for (i = 0; i < 10; i++){
    num_str[i] = j-- + '0';
  }
  num_str[i] = '\0';
  printf("%d\n", strcmp(num_str, "9876543210") == 0);
  // sort
  num_str = merge_sort(num_str);
  // verify
  printf("%d\n", strcmp(num_str, "0123456789") == 0);
}