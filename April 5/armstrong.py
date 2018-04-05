sum1=0
for i in range(1,1000):
    j=s=i
    sum1=0
    while i!=0:
        j=i%10
        i=int(i/10)
        sum1+=j**3

    if sum1==s:
        print(s)