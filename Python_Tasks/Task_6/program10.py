#Designer Door Mat

#https://www.hackerrank.com/challenges/designer-door-mat/problem
n, m = map(int, input().split())

# Upper half of the design
for i in range(1, n, 2):
    pattern = '.|.' * i
    print(pattern.center(m, '-'))

# Welcome message
print('WELCOME'.center(m, '-'))

# Lower half of the design
for i in range(n - 2, 0, -2):
    pattern = '.|.' * i
    print(pattern.center(m, '-'))