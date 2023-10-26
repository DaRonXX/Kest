
import random

tala = random.randint(1, 9)

while True:
    gisk = input("giskaðu á tölu milli 1 og 9: ")
    
    if gisk.isdigit():
        gisk = int(gisk)

        if 1 <= gisk <= 9:
            if gisk == tala:
                print("rétt gisk Tala", tala, "er rétt")
                break
            else:
                print("Rangt gisk, reyndu aftur")
print()



n = 0
while n <= 10:
    if n != 3 and n != 6:
        print(n)
    n += 1
print()


n = 2
while n <= 10:
    print(n)
    n += 2
print()


linur = 4
stjor = 5

while linur > 0:
    for i in range(stjor):
        print("*", end="")
    print()

    linur -= 1

