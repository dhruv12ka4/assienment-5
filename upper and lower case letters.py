def fun(a):
    n1 = 0
    n2 = 0
    for i in a:
        if i.islower():
            n1 = n1+1
        elif i.isupper():
            n2 = n2+1
    print("No. of lower case characters:",n1)
    print("No. of upper case characters:",n2)
    
s = str(input("enter any string:"))
print(fun(s))
