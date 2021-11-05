email=input('Please enter your email :')
list1=list(email)
a=0
b=0

for i in list1 :
    if i=="@" :
        a=1
    elif i=="." :
        b=1
if (a==0 or b==0) :
    print('Please enter valid email.')
if (a==1 and b==1) :
    print('Email you have entered is valid.')


