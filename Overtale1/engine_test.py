from libs import essentials
import time
import os
from random import randint

cmdlist = essentials.getcommandlist()

def cls(): 
    _ = os.system(cmdlist['clear'])

class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.level = 'level1'
        self.maxhp = 25
        self.hp = self.maxhp
        self.level = 1
        self.maxxp = self.level*10
        self.xp = 0

player = Player()

global_pal = {
'Y':'player'
}

levels = {
    'level1':{
    'pal':{' ':'air', 'W':'wall', 'E':'enemy'},
    'leveldat':[
    'WWWWWWWW',
    'EEEEEEEE',
    '        ',
    'W    W W',
    'W      W',
    'W      W',
    'W      W',
    'WWWWWWWW'
    ],
    'tileattr':{},
    'stageattr':{}
    }
}

def collisioncheck(px, py, pal, dat):
    if pal[dat[py][px]] in ['wall']:
        return True
    else:
        return False

level = levels[player.level]

while True:
    leveldisp = ''
    cls()
    for i in range(0,8):
        for j in range(0,8):
            k = level['leveldat'][i][j]
            if [j,i] == [player.x,player.y]:
                leveldisp += 'Y'
            else:
                leveldisp += k
        leveldisp += '\n'
    print(leveldisp)
    inp = input('> ').lower()
    for i in inp:
        p_x = player.x
        p_y = player.y
        if i == 'w':
            if not collisioncheck(p_x, p_y-1, level['pal'], level['leveldat']):
                player.y -= 1
        if i == 's':
            if not collisioncheck(p_x, p_y+1, level['pal'], level['leveldat']):
                player.y += 1
        if i == 'a':
            if not collisioncheck(p_x-1, p_y, level['pal'], level['leveldat']):
                player.x -= 1
        if i == 'd':
            if not collisioncheck(p_x+1, p_y, level['pal'], level['leveldat']):
                player.x += 1
        if level['pal'][ level['leveldat'][p_y][p_x+1]] == 'enemy':
            pass
