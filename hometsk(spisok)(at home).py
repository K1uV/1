import math

a = str("Apple")
b = str("Yuogurt")
c = str("Salo")
d = str("Voda")
#_________________________________________________________________________________________________
print("☰"*100)
print(" "*100)

print(a)
print(b)
print(c)
print(d)

print(" "*100)
print('☰'*100)
print(" "*100)


print(a,b,c,d)
print(" "*100)


lis = list(" 'Apple','Yuogurt','Salo','Voda'")
vvod = str(input("Введите название товара = "))

if bool(vvod) == lis:
    print("Есть такой товар!")
else:
    print("Нету такого товара!")



#Сделана проверка :)




print(" "*100)
print('☰'*100)
print(" "*100)




tovar = str("'Apple','Yuogurt','Salo','Voda'")

if 'Apple' in tovar:
    print("Яблоки есть!")
else:
    print("Яблок нету(")



if 'Yuogurt' in tovar:
    print("Йогурт есть есть!")
else:
    print("Йогурта нету(")


if 'Salo' in tovar:
    print("Сало есть!")
else:
    print("Сала нету(")


if 'Voda' in tovar:
    print("Вода есть!")
else:
    print("Воды нету(")

#Сделана проверка :)


print("  "*50)
print("  "*50)
print('☰'*100)
print("  "*50)
#___________________________________________________________________________________________________


Apple = 3
Yuogurt = 20
Salo = 50
Voda = 5
all_value = (Apple+Yuogurt+Salo+Voda)
print('Общее количество товара :',all_value)

print("  "*50)
print("  "*50)
print('☰'*100)
print("  "*50)

friends = {
    ("Vasya") : "Apple",
    ("Stopa") : "Yuogurt",
    ("Lila") : "Salo",
    ("Vanya") : 'Voda',
}

print(friends)
#_____________________________________________________________________________________________________

name1 = 'Vasya'
name2 = 'Stopa'
name3 = ' Lila'
name4 = 'Vanya'

print('☰'*100)

print(f"Apple is for {name1}")
print(" "*100)

print(f"Yuogurt is for {name2}")
print(" "*100)

print(f"Salo is for {name3}")
print(" "*100)


print(f"Voda is for {name4}")
print(" "*100)
print('☰'*100)




# До этого момента сделано на занятии
# До этого момента сделано на занятии
# До этого момента сделано на занятии
# До этого момента сделано на занятии
# До этого момента сделано на занятии
# До этого момента сделано на занятии
# До этого момента сделано на занятии


#_______________________________________________________________________________________________________

Apple = 4
Yuogurt = 15
Salo = 40
Voda = 5
all_sum = (Apple+Yuogurt+Salo+Voda)
print("Общая цена товара: ",all_sum)
print("Цена яблока:",Apple)
print("Цена йогурта: ",Yuogurt)
print("Цена сала: ",Salo)
print("Цена воды: ",Voda)

print(" ")
print('☰'*100)

#_______________________________________________________________________________________________

import math

Ap = 4
Yu = 15
Sa = 40
Vo = 5

A = int(input("Введите количество Apple: "))
B = int(input("Введите колчество Yuogurt: "))
C = int(input("Введите количество Salo: "))
D = int(input("Введите количество Voda: "))

z1 = (A*Ap)
z2 = (B*Yu)
z3 = (C*Sa)
z4 = (D*Vo)
z5 = (z1+z2+z3+z4)


money_vasya = int(10)
money_stopa = int(5)
money_lila = int(200)
money_vanya = int(20)

print(" ")
print('☰'*100)


if money_vasya <= z5:
    print("Vasya can't buy this stuff")
else:
    print('Vasya buy all that stuff')
print('')
if money_stopa <= z5:
    print("Stopa cant't buy that stuff")
else:
    print("Stopa buy all that stuff")

print('')

if money_lila <= z5:
    print("Lila can't buy that stuff")
else  :
    print("Lila  buy that stuff")

print('')

if money_vanya <= z5:
    print("Vanya can't buy that stuff")
else  :
    print("Vanya  buy that stuff")

print(" ")
print('☰'*100)
print(' ')


#

print("Цена яблок на выходе: ",z1)
print("Цена йогурта на выходе: ",z2)
print("Цена сала на выходе: ",z3)
print("Цена воды на выходе: ",z4)

print(" ")


#_________________________________________________________________________________________________________

print("  "*50)
print("☰"*100)
print("  "*50)

print(f"{name1} bring Apple to {name2} and {name2} пабыраму продал его на базаре)")

print(" ")