import random
import sys

def play_guess_number():
    # Генерация случайного числа
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    print("Игра 'Угадай число'")
    print("Я загадал число от 1 до 100")
    print(f"У тебя {max_attempts} попыток")
    
    # Игровая логика: цикл с ограничением попыток
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nОсталось попыток: {remaining}")
        
        # Запрос ввода с валидацией
        try:
            guess = int(input("Твое предположение: "))
        except ValueError:
            print("Ошибка: Введи целое число\n")
            continue
        
        # Валидация диапазона
        if guess < 1 or guess > 100:
            print("Ошибка: Число должно быть от 1 до 100. Попытка не потрачена.\n")
            continue
        
        attempts += 1
        
        # Проверка и подсказки
        if guess == secret_number:
            print(f"\nПоздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            return True
        elif guess < secret_number:
            print("Слишком маленькое. Попробуй больше.\n")
        else:
            print("Слишком большое. Попробуй меньше.\n")
    
    # Завершение при исчерпании попыток
    print(f"\nИгра окончена. Загаданное число было {secret_number}")
    print("В следующий раз повезет!")
    return False

# Главная функция
def main():
    
    while True:
        play_guess_number()
        print("\nСыграем еще раз?")
        again = input("Введите 'да' для новой игры или 'нет' для выхода: ").lower()
        if again != "да":
            print("Спасибо за игру!")
            break
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()