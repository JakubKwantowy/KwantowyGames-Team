from libs import essentials
import time
import os
from random import randint

clist = essentials.getcommandlist()

def cls():
    _ = os.system(clist['clear'])
    
cls()

print('Made with Python 3')
time.sleep(2)
cls()
print('Made and Published by')
time.sleep(2)
cls()
print()
print('Kwantowy TM')
print('   Games')
time.sleep(2)
cls()
print('                /\\/\\')
print('Kwantowy TM    <BOOM>')
print('   Games       <BOOM>')
print('                \\/\\/')
time.sleep(0.25)
cls()
print()
print('Kwantowy TM    .    .')
print('   Games         .')
print()
time.sleep(0.75)
cls()
print()
print('Kwantowy TM')
print('   Games ')
print()
time.sleep(5)
cls()
if not bool(randint(0,2)):
    print('Ahhhhhh Hohoho!')
    time.sleep(1)
cls()
print('###############')
print('# OVERTALE I: #')
print('#  DIMENSIONS #')
print('###############')
time.sleep(5)
playing = True
sel = 0
menu_e = ['Spielen','Schließen']
while playing:
    cls()
    print('###############')
    print('# OVERTALE I: #')
    print('#  DIMENSIONS #')
    print('###############\n')
    print('w,s Wahl Wechseln')
    print('e Wählen\n')
    essentials.selectdisplay(menu_e,sel)
    eingabe = input('> ').lower()
    for i in eingabe:
        if i == 'e':
            if sel == 1:
                playing = False
            elif sel == 0:
                os.system('python3 gamedat.py')
        else:
            sel = essentials.keyselect('s','w',i,sel,1,0,1)
