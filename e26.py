n=int(input("Donner un nombre : "))
while n<=0 :
    n=int(input("Donner un nombre positif non null: "))
s=0
for i in range(1,n* 2,2):
    s=s+(i**2)
print("le resultat est : ",s)