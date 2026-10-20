#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input values
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

# Find the symmetric difference using the symmetric_difference() method (or the ^ operator)
sym_diff = a.symmetric_difference(b)

# Print the sorted elements one per line
for num in sorted(sym_diff):
    print(num)