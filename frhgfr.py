n=int(input())
k=int(input())
r=0
p=1
while n!=0 and k!=0:
    if n%2 != 0:
        r=r + int(n/10)%10*p
        p=p*10
    else:
       k=k-1
    n = int(n / 10)
print(r)


