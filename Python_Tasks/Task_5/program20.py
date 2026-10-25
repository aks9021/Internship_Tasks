#Piling Up!

#https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

def piling_up(blocks):
    blocks = deque(blocks)
    last = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube > last:
            return "No"

        last = cube

    return "Yes"


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        blocks = list(map(int, input().split()))
        print(piling_up(blocks))