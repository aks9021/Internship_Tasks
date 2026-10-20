#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicates by converting to a set, then sort the unique scores
    unique_scores = sorted(set(arr))
    
    # The runner-up score is the second highest value (second from the last)
    print(unique_scores[-2])