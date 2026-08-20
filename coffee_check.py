coffees = [0,2,3,4,5,-6]

for coffee in coffees:
    if coffee < 0 :
        print(f"{coffee} чашек - Ошибка данных: количество не может быть отрицательным ")
    elif coffee == 0:
        print(f"{coffee} чашек - Срочно варить!!!") 
    elif 1 <= coffee <=3:
        print(f"{coffee} чашек - В Норме")
    else: 
        print(f"{coffee} чашек - Осторожно, перебор!")