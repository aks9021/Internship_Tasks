#Introduction to Sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # Convert the array to a set to get distinct heights and eliminate duplicates
    distinct_heights = set(array)
    
    # Compute the average and round it to 3 decimal places
    avg = sum(distinct_heights) / len(distinct_heights)
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)