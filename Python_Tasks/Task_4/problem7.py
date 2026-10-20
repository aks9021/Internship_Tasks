#String Split and Join
#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Split the string on spaces and join it back with a hyphen
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)