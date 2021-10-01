from libs import essentials
import time
import os
from random import randint
clist = essentials.getcommandlist()

def cls():
    _ = os.system(clist['clear'])

prokey = ['KG','OVERTALE1','OF']
playing = True
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.max_hp = 0
        self.xp = 0
        self.lvl = 0
        self.max_xp = 0
        self.inventory = [0]
        self.status_effects = []
        self.quests = []
        self.advancements = []
        self.attack = 0
        self.defense = 0
        self.equipment = [None,None,None,None,[None,None]]
        self.pos = {
        'x':0,
        'y':0,
        'type':None,
        'sector':None,
        'id':''
        }

sel = 0
if os.path.exists('sdata/player.ini'):
    menu_e = ['Neues Spiel','Fortfahren','Zurück']
    max_sel = 2
else:
    menu_e = ['Neues Spiel','Zurück']
    max_sel = 1   
    
while playing:
    cls()
    print('Wähle bitte\n')
    essentials.selectdisplay(menu_e,sel)
    eingabe = input('> ').lower()
    for i in eingabe:
        if i == 'e':
            if max_sel == 1:
                if sel == 1:
                    playing = False
        else:
            sel = essentials.keyselect('s','w',i,sel,1,0,max_sel)