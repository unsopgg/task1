# список книг {назв.книги: автор}

# список читателей {имя: {назв.книги: автор}}

# функция выводит инфу о читателях и книгах

# функция регистрирует читателя

# функция которая возвращает книгу

# функция менеджер

booklst = {'book1': 'author1', 'book2': 'author2', 'book3': 'aythor3'}

readerlst = {}

def br():
    global booklst
    global readerlst
    print(f'Список книг: {booklst}')
    print(f'Список читателей: {readerlst}')
def reg(name, take):
    global booklst
    global readerlst
    readerlst[name] = {take: booklst[take]}
def btog():
    global booklst
    global readerlst
    ta = input(f'Какую книгу вы хотите получить? Выберите из \n {booklst} \n Введите только название:')
    if ta in booklst:
        name = input(f'Введите ваше имя: ')
        reg(name, ta)
        booklst.pop(ta)
        print('Ваша заявка успешно оформлена!')
        br()
def manager():
    global booklst
    global readerlst
    ch = input('Вы хотите взять книгу или вернуть? Ведите "взять" или "вернуть": ').lower()
    if ch == 'взять':
            btog()
    elif ch == 'вернуть': 
        name = input('Введите имя: ')
        if name in readerlst:
            choise = input(f'Вы хотите вернуть: {readerlst[name]}? да/нет: ')
            inp = readerlst.values([0])
            if choise == "да":
                booklst.update(inp)
                br()
                readerlst.pop(inp)
                print('Вы вернули книгу')
            elif ch == 'нет':
                print('lol')
manager()













