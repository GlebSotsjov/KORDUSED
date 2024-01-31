
#1

n=int(input("sisestage number vahemikus 1 kuni 9:"))
for _ in range(n):
    print("^---^")
    print("( o o )")
    print(" ! = !/)")

 #2

n = int(input("Sisestage number n: "))
power = int(input("Sisestage astme eksponent: "))

result = 1
while result <= n * 100:
    print(f"{n}^{power} = {result}")
    power += 1
    result *= n
   
 #3
import random
from sys import getswitchinterval

hinded = [random.randint(1, 10) for _ in range(20)]

esimene_hinne = hinded[0]
viimane_hinne = hinded[0]

for hinne in hinded:
    if hinne < esimene_hinne:
        esimene_hinne = hinne
    elif hinne > viimane_hinne:
        viimane_hinne = hinne

print(f"Minimaalne hinne: {esimene_hinne}")
print(f"Maksimaalne hinne: {viimane_hinne}")
 #4
amööbas = 1

for tund in range(3, 25, 3):
    amööbas *= 2
    print(f"{tund} tunni pärast on {amööbas} amööbi")
 #5
K = int(input("Sisestage kotletide arv: "))
M = int(input("Sisestage kotletide arv ühel pannil: "))

pannid = 0
jaanud_kotletid = K

while jaanud_kotletid > 0:
    jaanud_kotletid -= M
    pannid += 1

print("Täispannide arv:", pannid)
print("Jäänud kotletid viimasel pannil:", M + jaanud_kotletid)