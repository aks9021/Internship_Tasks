#Word Order

#https://www.hackerrank.com/challenges/word-order/problem
if __name__ == '__main__':
    n = int(input())

    words = {}

    for i in range(n):
        word = input().strip()

        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(len(words))
    print(*words.values())