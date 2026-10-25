#No Idea!

#https://www.hackerrank.com/challenges/no-idea/problem
import sys

def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    m = int(input_data[1])

    arr = list(map(int, input_data[2:2+n]))

    A = set(map(int, input_data[2+n:2+n+m]))
    B = set(map(int, input_data[2+n+m:2+n+2*m]))

    happiness = sum((x in A) - (x in B) for x in arr)

    print(happiness)


if __name__ == '__main__':
    solve()