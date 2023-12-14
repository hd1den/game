import os
import random   
print('Привет! Я загадал слово, твоя задача угадать его по буквам.')
print('У тебя 10 попыток. Удачи! ')

input(" * Нажми Enter, чтобы продолжить * ")

word_string = """чоколадка машина дождь молоко кола спрайт вода телефон мышка 
камера деньги булавка 
слиток банк ножницы школа работа бмв поко айфон гномик 
мерседес банан речка точилка математик 
англисик русик игра стандофф
 пабг кс2 валорант тикток вайфай"""
word_list = word_string.split()

hp = 10


word = random.choice(word_list)

user_symb = ""

letters = []

while hp > 0:
    os.system('cls')
    # объявляем флажок
    is_win = True
    # 
    for symb in word:
        if symb  in letters:
            print(symb, end =" ")
        else:
            print("*", end =" ")
            # РОНЯЕМ ФЛАЖОК 
            is_win = False

    if is_win == True:
        print("\nВы победили")
        break


    user_symb = input("\nВведите букву: ")
    # добавляем букву в список
    letters.append(user_symb)


    if user_symb not in word:
        hp -= 1
        if hp == 0:
            print("Вы проиграли, было загадано слово", word)
            


        else:
            print("Осталось попыток", hp) 
            input(" * Нажми Enter, чтобы продолжить * ")


   