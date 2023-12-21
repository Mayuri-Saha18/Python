print("thanks for the pizza")
size=input()
pepproni=input()
cheeze=input()

bill=0
if size=="S":
    bill+=12
elif size=="M":
    bill+=15
else:
    bill+=20

if pepproni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if cheeze=="Y":
    bill+=1

print("your final bill is ${bill}")