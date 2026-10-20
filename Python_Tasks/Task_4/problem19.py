#collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

# Read input
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

# Count available shoe sizes
shoe_count = Counter(shoe_sizes)
total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    # If the shoe size is available in stock
    if shoe_count[size] > 0:
        total_earned += price
        shoe_count[size] -= 1  # Reduce stock by 1

# Print the total money earned
print(total_earned)