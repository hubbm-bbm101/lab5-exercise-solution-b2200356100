N=int(input('Please enter a number :'))
list1=list(range(1,N+1))
evenlist=[]
oddlist=[]
b=0
c=0

for i in list1 :
    int(i)
    a=i%2
    if a==0 :
        evenlist.append(i)
    else :
        oddlist.append(i)

for x in oddlist :
    b = b+x

for y in evenlist :
    c = c+y
    d = c/len(evenlist)
    int(d)

print('Sum of all odd numbers up to {}='.format(N),b)
print('Average of all even numbers up to {}='.format(N),d)




