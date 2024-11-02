#"Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр.
# Номера могут быть произвольной длины, с единственным условием, что количество цифр всегда чётно, например: 33 или 2341 и так далее.
#Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6. Билет с номером 231002 не является счастливым, так как 2 + 3 + 1 != 0 + 0 + 2


def lucky_ticket(ticket):
    if len(ticket) % 2 != 0:
        print ("Номер должен содержать чётное количество цифр")
        exit()
    else:
        sum1 = 0
        sum2 = 0
        for i in range(len(ticket) // 2):
            sum1 += int(ticket[i])
            sum2 += int(ticket[-i - 1])
        if sum1 == sum2:
            print("Счастливый билет")
        else:
            print("Не счастливый билет")


ticket = input("Введите номер билета: ")
print (lucky_ticket(ticket))

