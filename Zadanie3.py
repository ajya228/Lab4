#Напишите функцию, которая возвращает True, если введенная пользователем дата является магической, и False в обратном случае. Магической считается
# дата, в которой произведение дня и месяца равно двум последним цифрам года, например: 02.11.2022.

def magic_date(date):
    day, month, year = map(int, date.split('.'))
    if day * month == year % 100:
        return True
    else:
        return False

date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
print(magic_date(date))