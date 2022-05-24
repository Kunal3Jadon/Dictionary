#1..WAP to print sum of values of a dictionary
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
s=0
for i in d.values():
    s+=i
print(s)
#2..WAP to sort values of a dictionary
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
l=list(d.values())
l.sort()
print(l)
#3..WAP to merge two dictionaries
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
n1=int(input())
d1={}
for i in range(n1):
    key=input()
    value=int(input())
    d1.update({key:value})
d.update(d1)
print(d)
#4..WAP to input a number and check is it in values of dictionary
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
n1=int(input())
for i in d.values():
    if i==n1:
        print("number found")
        break
else:
    print("number not found")
#5..WAP to print multiplication of keys and values of a dictionary
n=int(input())
d={}
for i in range(n):
    key=int(input())
    value=int(input())
    d.update({key:value})
p=1
for i in d.values():
    p*=i
for i in d.keys():
    p*=i
print(p)
#6..WAP to print dictionary in format {1:1*n,2:2*n,3:3*n,4:4*n} where n is input number
n=int(input())
d={}
for i in range(1,n+1):
    d.update(i:i*n)
print(d)
