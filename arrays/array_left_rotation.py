import sys

def leftRotation(a, d):
    res = [0] * len(a)
    for i in range(len(res)):
        number_to_move_left = d % len(a)
        new_index = i - number_to_move_left
        if new_index < 0:
            new_index = len(a) + new_index
        res[new_index] = a[i]
    return res

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))
