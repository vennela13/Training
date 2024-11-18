
p=float(input("enter prinicipal "))
T=int(input("enter Time"))
R=int(input("enter rate of interest"))
I=p*T*R/100
print(I)


u=float(input("enter u"))
t=int(input("enter T"))
a=int(input("enter a"))
s=u*t+0.5*a*t*t
print(s)

l=int(input("enter length"))
w=int(input("enter width"))
Area=l*w
perimeter=2*(l+w)
print(Area)
print(perimeter)

c=int(input("enter celuis"))
F=1.8*c+32
print(F)

W=int(input("enter weight"))
H=float(input("enter Height in cm"))
BMI=W*H
print(BMI)

p=int(input("enter price"))
q=int(input("enter quantity"))
total=p*q
print(total)
sub_total=p*q*0.18
print(sub_total)

N=int(input("enter month"))
R=int(input("enter rate of interest"))
p=int(input("enter P"))
EMI=((p*R*(1+R)**N)/((1+R)**N)-1)
print(EMI)

import math
x1=int(input("enter x1"))
x2=int(input("enter x2"))
Y1=int(input("enter Y1"))
Y2=int(input("enter Y2"))

print(math.sqrt(4))
dist=math.sqrt((x2-x1)**2+(Y2-Y1))
print(dist)

