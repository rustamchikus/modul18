ticket = int(input("Сколько билетов необходимо? "))
print("Укажите возраст каждого посетителя")
a = 0
for i in range(ticket):
    age = int(input("Введите возраст: "))
    if age < 18:
        a += 0
    elif 18 <= age < 25:
        a += 990
    else:
        a += 1390
if ticket > 3:
    b = 0.9
else:
    b = 1
print("Сумма к оплате: ", a * b)