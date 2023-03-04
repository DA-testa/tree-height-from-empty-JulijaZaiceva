# python3

import sys
import threading

def compute_height(n, parents):
    max_height = 0
    if n == -1:
        return 0
    else:
        max_height += 1
        max_height += compute_height(parents[n], parents)
    return max_height

def main():
    count = 0
    num = 0
    txt = input()
    if txt[0]=='I':
        count = int(input())
        num = input().split()
    if txt[0]=='F':
        path = input()
        file = open("./test/"+path,mode ="r")
        lines = file.readlines()
        print(lines)
        count = int(lines[0])
        print(count)
        num = lines[1]
        print(num)
        
    num_list = list(map(int, num ))
    max_height = 0
    for i in range(count):
        height = compute_height(i, num_list)
        if height > max_height:
            max_height = height
    print(max_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
