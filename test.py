# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2:
    new_input = raw_input
    print ('Replaced py2 input')
else:
    new_input = input
    print ('Replaced py3 input')

	
riddle=(u'Сколько бит в байте?', u'Какая самая популярная кодировка Unicode?', u'В какой системе счисления компьютер хранит числа')

print (riddle)
i = 0
for rid in riddle:
    print rid