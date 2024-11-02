
def flames(n1, n2):
    res = ""
    
    if len(n1) > len(n2):
        n1, n2 = n2, n1

    stack1 = list(n1)
    stack2 = list(n2)

    print(stack1)
    print(stack2)

    for i in stack1:
        if i in stack2:
            stack1.remove(i)
            stack2.remove(i)

    print(stack1)
    print(stack2)

    total  = int(len(stack1) + len(stack2))

    print(total)

    return res

print("~~FLAMES~~")
n1 = input("Enter Name 1 : ")
n2 = input("Enter Name 2 : ")

res = flames(n1,n2)

print(f"{res}")