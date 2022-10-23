
from math import factorial

from decimal import getcontext, Decimal

k = 200 # number of packets bought
m = 5 # number of stickers per packet
s = 670 # total number of stickers in the sticker album
l = 20 # total number of different stickers in my set of interest
n = 20 # total number of stickers I get

def comb(n,k):
    if (k>n):
        return(0)
    else:
        result = factorial(n) // factorial(k) // factorial(n-k)
        return (result)


# como varia a probabilidade de sucesso em obter n ou mais figurinhas (scroll) com o número de pacotes comprados? (3)
# comprando-se k pacotes (scroll), qual o valor esperado para o número de figurinhas não-repetidas? (2)


# comprando-se k pacotes (scroll), qual a probabilidade de se completar o álbum? (1)
# número esperado de pacotes para completar o álbum (4)

context = getcontext()
getcontext().prec = 900

import csv
d = {}
fields = []
filename = "stickers2_pdf.csv"


with open(filename, "a", newline='') as file:
    fields = ["packets", "P(Xk(A)=n)", "P(Xk(A)<n)", "E(Xk(A))","P(Zn(A)=k)"]
    w = csv.DictWriter(file, fieldnames=fields)



    for k in range(1,2001):
        print(k)
        d["packets"] = k
        # (3)
        sum = 0
        for j in range(n+1):

            sum = context.add(sum, ((-1)**j) * context.multiply(comb(n, j) , context.power(context.divide(comb(s+n-l-j,m) , comb(s,m)), k)))

        p = abs(comb(l,n) * sum)
        print(f"P(Xk(A)=n) = {p:.6f}") # (3)

        d["P(Xk(A)=n)"] = round(float(p),6)

        sum = 0
        for j in range(n):
            sum = context.add(sum, ((-1)**(n-j+1)) * context.multiply(comb(l,j),context.multiply(comb(l-j-1,l-n),context.power(context.divide(comb(s-l+j,m),comb(s,m)),k))))
        p = sum
        print(f"P(Xk(A)<n) = {p:.6f}") # (3)

        d["P(Xk(A)<n)"] = round(float(p),6)

        # (2)
        e = l*(1-(1-m/s)**k)
        print(f"E(Xk(A)) = {e:.6f}") # (2)

        d["E(Xk(A))"] = round(float(e),6)

        # (1)
        sum = 0
        for j in range(n):
            temp = context.divide(comb(s-l+j,m),comb(s,m))
            temp = context.power(temp,k-1) if k > 1 else 0
            temp = context.multiply(temp, context.divide(context.subtract(comb(s,m),comb(s-l+j,m)),comb(s,m)))
            temp = context.multiply(temp, comb(l-j-1,l-n))
            temp = context.multiply(temp, comb(l,j))
            temp = temp * (-1)**(n-j+1)
            sum = context.add(temp, sum)

        p = sum
        print(f"P(Zn(A)=k) = {p:.6f}") # (1)

        d["P(Zn(A)=k)"] = round(float(p),6)

        w.writerow(d)
        d.clear()
        print()


# (4)

pos = []
neg = []
sum = 0
for j in range(1,s+1):
    sum = context.add(sum, ((-1)**(j+1)) * context.divide(comb(s,j), context.subtract (comb(s,m), comb(s-j,m))))
sum *= comb(s,m)
e = sum
print(f"E(Zn(A)) = {e:.6f}") # (1)

print()




