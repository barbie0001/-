import math
print("�� ������� ���������� �����������")
print("�������� ��������:")
print("1. ��������")
print("2. ���������")
print("3. ���������")
print("4. �������")
print("5. �����")
print("6. �������")
print("7. �������")
print("8. ���������� ������")
print("9. ���������� � �������")
print("10. ���������")
print("0. �����")

choice = input("������� ����� �������� (0-10): ")

if choice == "0":
        print("�� ������� ���������� �����������")
        

elif choice in ['1', '2', '3', '4']:
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))

        if choice == "1":
            result = num1 + num2
            print("��������� ��������: ", result)
        elif choice == "2":
            result = num1 - num2
            print("��������� ���������: ", result)
        elif choice == '3':
            result = num1 * num2
            print("��������� ���������: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("��������� �������: ", result)
            else:
                print("������: ������� �� ����!")

elif choice in ['5', '6', '7']:
        angle = float(input("������� �������� ���� (� ��������): "))
        radian = math.radians(angle)

        if choice == '5':
            result = math.sin(radian)
            print("��������� ������: ", result)
        elif choice == '6':
            result = math.cos(radian)
            print("��������� ��������: ", result)
        elif choice == '7':
            result = math.tan(radian)
            print("��������� ��������: ", result)

elif choice == '8':
        number = float(input("������� ����� ��� ���������� ����������� �����: "))
        result = math.sqrt(number)
        print("��������� ����������� �����: ", result)
     
elif choice == '9':
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        result = num1**num2
   
elif choice == '10':
       num2 = float(input("������� ����� ��� ����������: "))
       result = math.factorial(num2)
       print("��������� ����������:", result)
        
else:
        print("������������ ����! ���������� �����.")
