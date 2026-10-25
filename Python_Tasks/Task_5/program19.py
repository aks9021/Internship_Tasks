#Merge the Tools!

#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]

        result = ""
        seen = set()

        for char in substring:
            if char not in seen:
                result += char
                seen.add(char)

        print(result)




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)