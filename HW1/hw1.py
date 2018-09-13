
# coding: utf-8

# In[ ]:


import random 
import collections

tried_letters = []


# In[ ]:


# Рисуем пошагово человечка в виде элементов массива
def drawGallows():
    gallows = ['''
    
    
    
    
          _
     ____|_|_____
   ''', '''
     ______
    |
    |
    |
    |
    |     _ 
    |____|_|___
    ''','''
     ______
    |     |
    |     |
    |     
    |
    |     _ 
    |____|_|___
    ''', '''
     ______
    |     |
    |     |
    |     O
    |     
    |     _ 
    |____|_|___
    ''', '''
     ______
    |     |
    |     |
    |     O
    |     |
    |     _ 
    |____|_|___
    ''', '''
     ______
    |     |
    |     |
    |    \O
    |     |
    |     _ 
    |____|_|___
    ''','''
     ______
    |     |
    |     |
    |    \O/
    |     |
    |     _ 
    |____|_|___
    ''', '''
     ______
    |     |
    |     |
    |    \O/
    |     |
    |    /_ 
    |____|_|___
    ''', '''
     ______
    |     |
    |     |
    |    \O/
    |     |
    |    /_\    
    |____|_|_____
    ''', '''
     ______
    |     |
    |     |
    |    \O/
    |     |
    |    / \    
    |___________
        ''']

    return gallows


# In[ ]:


# программа принимает на вход номер темы из предложенных, если формат ввода неверный - 
# сообщает об этом и предлагает выбор снова и снова. Возвращает список слов из файла
def topic():
    theme = input('Введите номер желаемой темы: \n 1) Журналистика \n 2) Византийская книжность \n 3) Французская кухня \n ')
    while True:
        if theme == "1" or theme == '2' or theme == '3':
            with open(theme + '.txt', 'r', encoding='utf-8') as f:
                f = [line.strip() for line in f]
            break
        else:
            theme = input('Внимание! Ввести нужно только номер:     \n 1) Журналистика \n 2) Византийская книжность \n 3) Французская кухня \n ')
    return f


# In[ ]:


#Выбираем рандомное слово из списка
def getWord(topic):
    word = random.choice(topic)
    return word


# In[ ]:


# Проверяем введенные символы: одна буква, кириллица, регистр не важен
def checkLetter():
    while True:
        user_attempt = input('Введите букву, которая, по вашему мнению, есть в этом слове: ').lower()
        tried_letters.append(user_attempt)
        if user_attempt in tried_letters[:-1]:
            print('Вы уже пробовали эту букву, забыли?')
        elif len(user_attempt) > 1:
            print('Кажется, здесь не одна буква, я запутался...')
        elif len(user_attempt) == 0:
            print('По-моему, вы ничего не написали. Все же придумайте букву!')
        elif user_attempt not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Такой буквы в русском алфавите нет!')
        else:
            return user_attempt


# In[ ]:


# Принимаем на вход букву, которая прошла все проверки. Если она есть в слове - открываем ее. 
# Всего 10 попыток, если введена не буква или буква, которая уже была, не считается за попытку
# Возвращает кортеж из угаданного слова (или его части) и загаданного слова
def game(word):
    puzzle = len(word) * '_ '
    print(puzzle)
    # заведем счетчик использованных попыток
    attempts = 0
    while attempts < 10 and ''.join(puzzle.split()) != word:
        guess = checkLetter()
        if guess in word:
            for index in range(len(word)):
                if word[index] == guess:
                    puzzle = puzzle[:index*2] + word[index] + ' ' + puzzle[(index+1)*2:]
            print(puzzle)
        else:
            print('Такой буквы в слове нет!')
            print(puzzle)
            attempts += 1
            print(drawGallows()[attempts-1])
            if attempts >= 6 and attempts <= 8:
                print('У вас осталось ', 10 - attempts, 'попытки')
            elif attempts == 9:
                print('У вас осталась', 10 - attempts, 'попытка')
            else:
                print('У вас осталось', 10 - attempts, 'попыток')
    return puzzle, word


# In[ ]:


# Сравниваем угаданную часть и загаданное слово. Если они совпадают, выигрыш
def checkWin(game):
    if ''.join(game[0].split()) == game[1]:
        print('Поздравляю! Вас не успели повесить!')
    else:
        print('О нет! Вы проиграли... Это было слово "', game[1], '" Попробуйте сыграть еще раз.')
    goOn()


# In[ ]:


# Предлагаем продолжить игру
def goOn():
    tried_letters.clear()
    wish = input('Если хотите продолжить игру, введите "да": ')
    if wish.lower() == "да":
        checkWin(game(getWord(topic())))
    else:
        wish = input('Вы действительно заканчиваете игру? Введите "да" или "нет"')
        if wish.lower() == 'да':
            print('До свидания!')
        elif wish.lower() == "нет":
            checkWin(game(getWord(topic()))) 
        else:
            print('Я вас не совсем понимаю... Поэтому на всякий случай сыграем еще раз')
            checkWin(game(getWord(topic())))                


# In[ ]:


def main():
    return checkWin(game(getWord(topic())))

if __name__== '__main__':
    main()

