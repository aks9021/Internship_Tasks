#Find a string

#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    
    # Iterate through the string up to the point where the substring can still fit
    for i in range(len(string) - sub_len + 1):
        # Check if the slice of the string matches the substring
        if string[i:i + sub_len] == sub_string:
            count += 1
            
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)