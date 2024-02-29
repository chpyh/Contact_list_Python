# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле. 1. Программа должна выводить данные 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    
    while (choice!="8"):
        if choice=="1": # "1. Отобразить весь справочник\n"
            print(phone_book)
        elif choice=="2":
            info =input('Введите фамилию')
            print(find_by(phone_book,info))
        elif choice=="3":
            last_name=input('Введите фамилию ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice=="4":
            user_data=input('Введите данные абонента через запятую')
            add_user(phone_book,user_data)
        elif choice=="5":
            write_txt('phonebook.txt',phone_book)
        elif choice=="6":
            last_name=input('Введите фамилию ')
            delete_by_lastname(phone_book,last_name)  
        elif choice=="7":
            break
            

        choice=show_menu()


def show_menu():
    # тут немного поправила действия для оптимизации
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии, имени или телефону\n"
          "3. Изменить номер телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента\n"
          "7. Закончить работу")
    choice = input()
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.strip().split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) )
           phone_book.append(record)
    return phone_book

# далее мой полет фантазии
def find_by (phone_book,info):
    for contact in phone_book:
        for key in contact:
            if info in contact[key]:
                return contact
    return "Контакт не найден"        
                 

def change_number(phone_book,last_name,new_number):
    for contact in phone_book:
        if last_name in contact['Фамилия']:
            contact['Телефон'] = new_number
            return contact

def add_user(phone_book,user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_contact = dict(zip(fields, user_data.strip().split(',')))
    phone_book.append(new_contact)

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def delete_by_lastname(phone_book,last_name):
    for contact in phone_book:
        if last_name in contact['Фамилия']:
            number = phone_book.index(contact)
            phone_book.pop(number)


work_with_phonebook()
