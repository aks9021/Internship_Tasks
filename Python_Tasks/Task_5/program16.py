#collections.Counter()

#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

if __name__ == '__main__':
    X = int(input())

    shoe_sizes = list(map(int, input().split()))

    # Count available shoes of each size
    shoe_count = Counter(shoe_sizes)

    N = int(input())
    earnings = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoe_count[size] > 0:
            earnings += price
            shoe_count[size] -= 1

    print(earnings)