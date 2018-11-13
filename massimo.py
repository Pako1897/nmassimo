cont=2
cont=int(cont)

n1=input("Inserire numero: ")
n2=input("Inserire numero: ")
n1=int(n1)
n2=int(n2)

if n1>n2:
 max=n1;
elif n2>n1:
 max=n2
else:
 max=n1

while cont<9:
 n3=input("Inserire numero: ")
 n3=int(n3)
 if n3>max:
  max=n3
 cont+=1

print(max)
  
   