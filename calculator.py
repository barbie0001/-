import math
print("Вы открыли инженерный калькулятор")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Синус")
print("6. Косинус")
print("7. Тангенс")
print("8. Квадратный корень")
print("9. Возведение в степень")
print("10. Факториал")
print("0. Выход")

choice = input("Введите номер операции (0-10): ")

if choice == "0":
        print("Вы закрыли инженерный калькулятор")
        

elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            result = num1 + num2
            print("Результат сложения: ", result)
        elif choice == "2":
            result = num1 - num2
            print("Результат вычитания: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат умножения: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Результат деления: ", result)
            else:
                print("Ошибка: Деление на ноль!")

elif choice in ['5', '6', '7']:
        angle = float(input("Введите значение угла (в градусах): "))
        radian = math.radians(angle)

        if choice == '5':
            result = math.sin(radian)
            print("Результат синуса: ", result)
        elif choice == '6':
            result = math.cos(radian)
            print("Результат косинуса: ", result)
        elif choice == '7':
            result = math.tan(radian)
            print("Результат тангенса: ", result)

elif choice == '8':
        number = float(input("Введите число для извлечения квадратного корня: "))
        result = math.sqrt(number)
        print("Результат квадратного корня: ", result)
     
elif choice == '9':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1**num2
   
elif choice == '10':
       num2 = float(input("Введите число для факториала: "))
       result = math.factorial(num2)
       print("Результат факториала:", result)
        
else:
        print("Некорректный ввод! Попробуйте снова.")
