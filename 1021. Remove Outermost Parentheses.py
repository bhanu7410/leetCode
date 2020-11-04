s="(())"
x=''
v=''
a=0
b=0
for i in s:
    x+=i
    print(x+'1'+v)
    if i=='(':
        a+=1
    else:
        b+=1
    if a==b:
        v=x[1:-1]
        print(x+'2'+v)
        x=''
        print(x+'3'+v)


print(v)