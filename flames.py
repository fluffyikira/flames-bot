def getRes(total_steps):
    flameMap = {'F':'friends','L':'lovers','A':'affection','M':'marriage','E':'enemies','S':'sex'} 
    flames = ['F','L','A','M','E','S'] 
    start = 0
    while len(flames) > 1:
        indextopop =  (start + total_steps)%len(flames) - 1
        start = indextopop%len(flames)
        flames.pop(indextopop)
    
    return flameMap[flames[0]]

def flames(n1, n2):
    if len(n1) > len(n2):
        n1, n2 = n2, n1

    stack1 = list(n1)
    stack2 = list(n2)
    stack3,stack4 = stack1[:],stack2[:]

    for i in stack3:
        if i in stack4:
            stack1.remove(i)
            stack2.remove(i)

    total  = int(len(stack1) + len(stack2))

    res = getRes(total)

    return res

print("~~flames~~")
n1 = input("enter a name : ")
n2 = input("another one  : ")

res = flames(n1,n2)

print(f"{res}")