a=int(input())
for i in range(a):
    print("* " ,end="")
print()
for i in range(a-1):
    print("* ",end="")
    print("* " *(a-i-2),end="")
    print()