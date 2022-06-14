# Apoorv Varkute

ans=[]
for num in range(1,101):
    st1=str(num)
    x=int(st1)
    while (len(str(x))>1):
        sum=0
        st2=str(x)
        for i in range(len(st2)):
            sum=sum+(int(st2[i])**2)
        x=sum
    if x==1:
        ans.append(num)
    else:
        continue        