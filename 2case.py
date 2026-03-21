import math
import sys
# Отключение лимита на колличество цифр
sys.set_int_max_str_digits(0)

# Вычисление факториала
def calculate_factorial(n):

    return math.factorial(n)
# Запрос числа у пользователя
def get_number():

    while True:
        try:
            number = int(input("Введите положительное целое число: "))
            if number < 0:
                print("Ошибка: Число должно быть положительным\n")
                continue
            return number
        except ValueError:
            print("Ошибка: Введите целое число\n")

# Главная функция
def main():
    print("Программа вычисления факториала")
    number = get_number()
    
    try:
        result = calculate_factorial(number)
        print(f"\n{number}! = {result}")
            
    except MemoryError:
        print("\nОшибка: Недостаточно памяти")
    except Exception as e:
        print(f"\nОшибка: {e}")

# Ожидание ENTER    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()