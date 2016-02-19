# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2:
    new_input = raw_input
    print ('Replaced py2 input')
else:
    new_input = input
    print ('Replaced py3 input')

	
riddle = (u'Сколько бит в байте?', u'Какая самая популярная кодировка Unicode?', u'В какой системе счисления компьютер хранит числа')
answer = (u'8', u'utf-8', u'двоичной')
i = len (riddle)
print (u'Вам будет загадано %s загадок' % i)
mis_count = 0
mis = 0
while i:
    while True:
        print (riddle[i-1])
        ans = new_input()
        if ans == answer[i-1]:
            print (u'Отлично, верный ответ')
            i = i - 1
            break
        else:
            print (u'Ошибка, попробуй ещё раз')
            mis_count = mis_count + 1
            mis = mis + 1
            if mis > 3:
                print (u'Похоже, задача вам не дается, переходим к следующей')
                i = i - 1
                mis = 0
                break
            else:
                mis = mis + 1
            

print (u'Ошибок было %s' %mis_count)