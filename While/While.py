# While 
n=1
while n < 10 :
    print(f"Thiis Lop is {n} ")
    n+=1
print("End Loop")



# continue 
n=1
while n < 10 :
    n+=1

    if n==6 or  n==8 :
        continue
    print(f"Thiis Lop is {n} ")

print("End Loop")

# break 

n=-10
while n< 100:
    n+=1
    if n==80:
        break

    print(f"Can't continue in This Loop{n}")
print("This Loop End ")


bat_lvl=80
charge_lvl=100

while bat_lvl < charge_lvl :
    print(f'This Bat is chearged {bat_lvl}')
    bat_lvl+=1

else:
    print("Battrey is Max lvl")


bat_lvl=0
charge_lvl=100

while bat_lvl < charge_lvl :
    bat_lvl+=1

    if (bat_lvl==89):
        print("Battrey is Max lvl")
        break

    print(f'This Bat is chearged {bat_lvl}')

else:
    print("Battrey is Max lvl")
    