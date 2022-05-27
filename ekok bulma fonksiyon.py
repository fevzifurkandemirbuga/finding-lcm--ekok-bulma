def lcm(x,y):
    i=1
    if (y>x):
        while i!=y:
            if not((x*i)%y):
                result=x*i
            i+=1
    else:
        while i!=x:
            if not((y*i)%x):
                result=y*i
            i+=1
    return result
a=int(input("enter two number\n"))
b=int(input())
print("lowest common multiple:",lcm(a,b))