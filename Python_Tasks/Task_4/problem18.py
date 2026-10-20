#Lists
#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    L = []
    
    for _ in range(N):
        args = input().split()
        cmd = args[0]
        
        if cmd == 'print':
            print(L)
        else:
            # Dynamically call the list method (append, insert, remove, etc.)
            # with the remaining arguments converted to integers.
            getattr(L, cmd)(*(map(int, args[1:])))