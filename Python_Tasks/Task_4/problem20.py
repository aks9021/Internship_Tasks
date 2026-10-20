#No Idea!
#https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Parse the array and sets
    arr = [int(x) for x in input_data[2:2+n]]
    A = set(int(x) for x in input_data[2+n : 2+n+m])
    B = set(int(x) for x in input_data[2+n+m : 2+n+2*m])
    
    # Calculate happiness: 
    # (x in A) evaluates to 1 if True, 0 if False
    # (x in B) evaluates to 1 if True, 0 if False
    happiness = sum((x in A) - (x in B) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()