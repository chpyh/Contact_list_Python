def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)

        choice=show_menu()


def show_menu():
    print("\nР’С‹Р±РµСЂРёС‚Рµ РЅРµРѕР±С…РѕРґРёРјРѕРµ РґРµР№СЃС‚РІРёРµ:\n"
          "1. РћС‚РѕР±СЂР°Р·РёС‚СЊ РІРµСЃСЊ СЃРїСЂР°РІРѕС‡РЅРёРє\n"
          "2. РќР°Р№С‚Рё Р°Р±РѕРЅРµРЅС‚Р° РїРѕ С„Р°РјРёР»РёРё\n"
          "3. РќР°Р№С‚Рё Р°Р±РѕРЅРµРЅС‚Р° РїРѕ РЅРѕРјРµСЂСѓ С‚РµР»РµС„РѕРЅР°\n"
          "4. Р”РѕР±Р°РІРёС‚СЊ Р°Р±РѕРЅРµРЅС‚Р° РІ СЃРїСЂР°РІРѕС‡РЅРёРє\n"
		РёР·РјРµРЅРёС‚СЊ РґР°РЅРЅС‹Рµ
          "5. РЎРѕС…СЂР°РЅРёС‚СЊ СЃРїСЂР°РІРѕС‡РЅРёРє РІ С‚РµРєСЃС‚РѕРІРѕРј С„РѕСЂРјР°С‚Рµ\n"
          "6. Р—Р°РєРѕРЅС‡РёС‚СЊ СЂР°Р±РѕС‚Сѓ")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Р¤Р°РјРёР»РёСЏ', 'РРјСЏ', 'РўРµР»РµС„РѕРЅ', 'РћРїРёСЃР°РЅРёРµ']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
			#dict(( (С„Р°РјРёР»РёСЏ,РРІР°РЅРѕРІ),(РёРјСЏ, РўРѕС‡РєР°),(РЅРѕРјРµСЂ,8928) ))
  
	phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')















work_with_phonebook()
