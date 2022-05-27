#

def encryption():
    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(10): # 10 попыток првильно ввести правильно число
        away=int(input("Расшифрование (1), Шифрование(2) : "))
        if away!=1 and away!=2:
            print('Неправильные данные , выберите (1) или (2) ')
        else:
            break
    if away == 2:
        way=int(input("Способ шифрования:  Посимвольно(1) ,Блоками(2) ,Пословно(3):"))
        if way==1:
            smeshenie_1 = int(input('Шаг шифровки: '))
            message_1 = input("Сообщение для шифровки: ").upper()
            itog_1 = ''
            for i in message_1:
                mesto = alfavit_EU.find(i)
                new_mesto = mesto + smeshenie_1
                if i in alfavit_EU:
                    itog_1 += alfavit_EU[new_mesto]
                else:
                    itog_1 += i
            print ("Сообщение после шифрования: ")
            print (itog_1.lower())
        elif way==2:
            block=int(input("Введите количество элементов в одном блоке : "))
            for l in range (10):
                smeshenie_2 = input('Ключ шифровки: ')
                if len(smeshenie_2)!= block:
                    print("Вы ввели неправильный ключ , попробуйте заново ... ")
                    continue
                def proverka(smsmeshenie_2):
                    for i in range(len(smeshenie_2)):
                        for j in range(len(smeshenie_2)):
                            if smeshenie_2[i]== smeshenie_2[j] and i!=j or int(smeshenie_2[i])>=block:
                                print("Вы ввели неправильный ключ , попробуйте заново  ")
                                return 0
                    else:
                        return 1
                if proverka(smeshenie_2):
                    message_2 = input("Сообщение для шифровки: ")
                    break
                else:
                    continue
            if len(message_2) % block !=0:
                for i in range(block - len(message_2) % block) :
                    message_2=message_2+"\0"
            itog_2=""
            for i in range (len(message_2)//block):
                for j in range(block):
                    itog_2=itog_2 +message_2[i*block + int(smeshenie_2[j])]
            print("Сообщение после шифрования: ")
            print(itog_2)
        if way==3:
            block_3=int(input("Введите количество слов в одном блоке: "))
            for i in range(10):# 10 попыток првильно ввести правильно число (ключ)
                smeshenie_3 = input("Введите ключ щифрования:  ")
                if len(smeshenie_3) != block_3:
                    print("Вы ввели неправильный ключ , попробуйте заново ... ")
                    continue

                def proverka(smsmeshenie_3):
                    for i in range(len(smeshenie_3)):
                        for j in range(len(smeshenie_3)):
                            if smeshenie_3[i] == smeshenie_3[j] and i != j or int(smeshenie_3[i]) >= block_3:
                                print("Вы ввели неправильный ключ , попробуйте заново  ")
                                return 0
                    else:
                        return 1

                if proverka(smeshenie_3):
                    message_3 = input("Сообщение для шифровки: ")
                    break
                else:
                    continue
            sms_3 = str.split(message_3)

            if len(sms_3) % block_3 !=0:
                for i in range(block_3 - len(sms_3) % block_3) :
                    message_3=message_3+" \0"
            sms_3 = str.split(message_3)
            itog_3=""
            for i in range(len(sms_3) // block_3):
                for j in range(block_3):
                    itog_3 = itog_3 + " "+sms_3[i * block_3 + int(smeshenie_3[j])]
            print("Сообщение после шифрования: ")
            print(itog_3)
    if away==1:
        way = int(input("Способ расшифрования:  Посимвольно(1) ,Блоками(2) ,Пословно(3): "))
        if way == 1:
            smeshenie_1 = int(input('Шаг расшифровки: '))
            message_1 = input("Сообщение для расшифровки: ").upper()
            itog_1 = ''
            for i in message_1:
                mesto = alfavit_EU.find(i)
                new_mesto = mesto - smeshenie_1
                if i in alfavit_EU:
                    itog_1 += alfavit_EU[new_mesto]
                else:
                    itog_1 += i
            print("Сообщение после расшифрования: ")
            print(itog_1.lower())
        elif way==2:
            block=int(input("Введите количество элементов в одном блоке : "))
            for l in range (10):# 10 попыток првильно ввести правильно число ( ключ расшифровки)
                smeshenie_2 = input('Ключ расшифровки: ')
                if len(smeshenie_2)!= block:
                    print("Вы ввели неправильный ключ , попробуйте заново ... ")
                    continue
                def proverka(smsmeshenie_2):
                    for i in range(len(smeshenie_2)):
                        for j in range(len(smeshenie_2)):
                            if smeshenie_2[i]== smeshenie_2[j] and i!=j or int(smeshenie_2[i])>=block:
                                print("Вы ввели неправильный ключ , попробуйте заново  ")
                                return 0
                    else:
                        return 1
                if proverka(smeshenie_2):
                    message_2 = input("Сообщение для расшифровки: ")
                    break
                else:
                    continue

            itog_2=""
            r=""# вспомогательные элементы для создания ключа расшифровки ( обратного ключа шифрования)
            reverse=[0]*block
            for i in range(block):
                r=r + str(i)
            for i in range(block):
                reverse[int(smeshenie_2[i])]=r[i]
            for i in range (len(message_2)//block):
                for j in range(block):
                    itog_2=itog_2 +message_2[i*block + int(reverse[j])]
            s=itog_2.replace("\0","")
            print("Сообщение после шифрования: ")
            print(s)
        if way==3:
            block_3=int(input("Введите количество слов в одном блоке: "))
            for i in range(10):
                smeshenie_3 = input("Введите ключ шифрования:  ")
                if len(smeshenie_3) != block_3:
                    print("Вы ввели неправильный ключ , попробуйте заново ... ")
                    continue

                def proverka(smsmeshenie_3):
                    for i in range(len(smeshenie_3)):
                        for j in range(len(smeshenie_3)):
                            if smeshenie_3[i] == smeshenie_3[j] and i != j or int(smeshenie_3[i]) >= block_3:
                                print("Вы ввели неправильный ключ , попробуйте заново  ")
                                return 0
                    else:
                        return 1

                if proverka(smeshenie_3):
                    message_3 = input("Сообщение для расшифровки: ")
                    break
                else:
                    continue
            for i in range(2,len(message_3)):
                if  message_3[i]==" " and message_3[i-1]==" " and message_3[i-2]==" ":
                    message_3 = message_3[:i-1]+"/"+message_3[i:]

            sms_3 = str.split(message_3)  # Разделение строки на массив где элементы слова

            if len(sms_3) % block_3 !=0:# Дополнение до длины такой , чтобы нацело делилось на количетсво
                message_3 = message_3+" /"
            sms_3 = str.split(message_3)
            itog_3=""
            r=""# вспомогательные элементы для создания ключа расшифровки ( обратного ключа шифрования)
            reverse=[0]*block_3
            for i in range(block_3):
                r=r + str(i)
            for i in range(block_3):
                reverse[int(smeshenie_3[i])]=r[i]
            for i in range(len(sms_3) // block_3):# само "расшифрование"
                for j in range(block_3):
                    itog_3 = itog_3 + " "+sms_3[i * block_3 + int(reverse[j])]
            s=itog_3.replace("/"," ") # тут все понятно
            print("Сообщение после расшифрования: ")
            print(s)
encryption()