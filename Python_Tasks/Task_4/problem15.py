#Word Order
#https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict
import sys

def main():
    # Read all inputs from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    
    # Use OrderedDict to count occurrences while preserving insertion order
    word_counts = OrderedDict()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # Output the number of distinct words
    print(len(word_counts))
    
    # Output the occurrences of each distinct word separated by spaces
    print(*(word_counts.values()))

if __name__ == '__main__':
    main()