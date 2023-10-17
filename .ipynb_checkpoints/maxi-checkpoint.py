
def maximum(a,b):
    if a <b:
        max=b
    else:
        max=a
    print max #added for git
    return max

print(maximum(4,1))


def maximum3(a,b,c):
    max=maximum(a,b)
    max=maximum(max,c)
    print max #added for git
    return max


print(maximum3(4,12,1))

def maximum3_input():
    a=[]
    for i in range(0,3):
        b=int(input('Entier?'))  
        a.append(b) 
    max=maximum3(a[0],a[1],a[2])
    return max


print(maximum3_input())