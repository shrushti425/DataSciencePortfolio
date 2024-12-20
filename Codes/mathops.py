import math
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)
def dictionary(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    return d
def making():
    values=input()
    list1=values.split(',')
    tuples1=tuple(list1)
    print(list1,tuples1)
 

x=int(input())
print(factorial(x))
n=int(input())
print(dictionary(n))
making()
C=50
H=30
value=[]
i=[x for x in input().split(',')]
for d in i:
    value.append(str(int(round(math.sqrt(2*C*float(d)/H)))))
print(','.join(value))



