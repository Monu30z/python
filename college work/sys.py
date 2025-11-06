import sys
print(sys.version)
print(sys.argv)

print(sys.path)

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5)
print(sys.getrecursionlimit())
i = 0
def myfun():
    global i
    i=i+1
    print("my func",i)
    myfun()
myfun()  