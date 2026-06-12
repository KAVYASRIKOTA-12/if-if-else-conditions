a=str(input("value"))
if type(a) is str:
    print("true")
else:
    print("false")


#if -condition by using comparision operators
#<,>,<=,>=,!=.==
a=10
if a>1:
    print("true")
    
a=10
if a<1:
    print("true")
    
a=10
if a==10:
    print("true")
    
a=int(input("a value"))
if a>20:
    print("greater")
    
a=int(input("a value"))
if a<20:
    print("greater")
    
a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")

a=49
b=10
if a<b:
    print("greater")
    
a=10
b=10
if a==b:
    print("equal")
    
a=20
b=10
if a==b:
    print("equal")
    
a="python"
b="java"
if a!=b:
    print("not equal")
    
a=int(input("a value"))
if a!=20:
    print("greater")

#if-condition by using logical opertors
#and,or,not
a=3
b=4
if a<b and b>a:
    print("true")
    
a=3
b=4
if a<b or b>a:
    print("true")
    
a=7
b=4
if a>b or b<a:
    print("true")
    
a=8
b=5
if a!=b and b==a:
    print("true")
    
a=3
b=4
if a<=b or b>=a:
    print("true")
    
a=3
b=4
if not a>b and b<a:
    print("true")
    
a=3
b=4
if not a<b or b>a:
    print("true")
    
a=3
b=4
if not a==b or b!=a:
    print("true")
    
#if-condition by using identify operators
#is,is not
a=2
if type(a) is int:
    print("true")
    
a=2
if type(a) is not int:
    print("true")
    
a=int(input("a value"))
if type(a) is int:
    print("it is int")
    
a=int(input("a value"))
if type(a) is not int:
    print("it is int")
    
a=float(input("a value"))
if type(a) is float:
    print("it is int")
    
a=str(input("a value"))
if type(a) is str:
    print("it is str")
    
a=bool(input("a value"))
if type(a) is bool:
    print("it is bool")
    
a=bool(input("a value"))
if type(a) is not bool:
    print("it is bool")
    
#if-condition by usind membership operators
#in,not in
a=[10,20,30,40,50]
if 40 in a:
    print("true")
    
a=[10,20,30,40,50]
if 40 not in a:
    print("true")
    
a=[10,20,30,40,50]
if 10 not in a:
    print("false")
    
a=[10,20,30,40,50]
b=int(input("value"))
if b in a:
    print("true")

a=int(input("value"))
if 50 in a:
    print("true")

#if-else conditions by using comparision
a=20
b=40
if a>b:
    print("true")
else:
    print("false")
    
a=20
b=40
if a!=b:
    print("true")
else:
    print("false")
    
a=20
b=40
if a==b:
    print("true")
else:
    print("false")
    
a=int(input("value"))
b=int(input("value"))
if a>b:
    print("true")
else:
    print("false")
    
#if-else condition by using membership operators
a=[10,20,30,40,50]
if 50 in a:
    print("true")
else:
    print("false")
    
a=[10,20,30,40,50]
if 60 in a:
    print("true")
else:
    print("false")
    
a=[10,20,30,40,50]
b=int(input("value"))
if 60 in a:
    print("true")
else:
    print("false")
    
a=[10,20,30,40,50]
if 60 in a:
    print("true")
else:
    print("false")
    
#if-else condition by using identity operators 
a=30
if type(a) is int:
    print("true")
else:
    print("false")
    
a=30
if type(a) is  not int:
    print("true")
else:
    print("false")

a=int(input("value"))
if type(a) is int:
    print("true")
else:
    print("false")
    
a=str(input("value"))
if type(a) is str:
    print("true")
else:
    print("false")
    
a=str(input("value"))
if type(a) is not str:
    print("true")
else:
    print("false")



