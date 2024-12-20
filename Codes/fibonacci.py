import time
start=time.time()
def projection (n):
    a=10000
    b=15000
    if 0<n<=1:
        return a
    elif n<=2:
        return b
    else:
        return(projection(n-1) + projection(n-2))
try: 
    n=int(input('Enter the number of quarters\n'))
    if n<=0:
         raise Exception()
except:
        print('Enter a positive integer\n')
else:
    print(f'Projection over the years:')
    l1=[10000]
    for i in range(2,n+1):
        l1.append(projection(i))
    print(l1)
end=time.time()
print("Time taken for execution of code is:",(end-start)*10**3,"ms")