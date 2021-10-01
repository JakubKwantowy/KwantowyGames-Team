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
        self.xplevel = 1
        self.maxxp = self.level*10
        self.xp = 0
        self.attack = 5
        self.defense = 5
        self.inventory = ['Potion', 'Poison', 'HyperAttack', 'HyperDefense']

class Enemy:
    def __init__(self, name, maxhp, attack, defense, minxp, maxxp):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.attack = attack
        self.defense = defense
        self.minxp = minxp
        self.maxxp = maxxp

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

def getratio(bigmax, bigmin, mediummax):
    ration = bigmax/bigmin
    return mediummax/ration

def roundup(value):
    value = int(value)
    if bool(value):
        return value+1
    else:
        return 0

def backtoten(value):
    if value > 10:
        value = 10
    return value


def collisioncheck(px, py, pal, dat):
    if pal[dat[py][px]] in ['wall']:
        return True
    else:
        return False

def battle():
    randomint = randint(0,1)
    if randomint < 1:
        enemy = Enemy('Strong',35, 7, 8, 10, 20)
    else:
        enemy = Enemy('Weak',10, 4, 3, 0, 7)
    cls()
    print('BATTLE!')
    time.sleep(2.5)
    cls()
    fordisp = ['@'*backtoten(roundup(getratio(player.maxhp, 10, player.hp))),
               '@'*backtoten(roundup(getratio(enemy.maxhp, 10, enemy.hp)))]
    print(enemy.name + ' VS Kw')
    print('    Enemy Hp: '+str(fordisp[1])+' '+str(enemy.hp)+'/'+str(enemy.maxhp))
    print('Player Hp: '+str(fordisp[0])+' '+str(player.hp)+'/'+str(player.maxhp))
    input()


plevel = player.level

level = levels[plevel]
playing = True

while playing:
    leveldisp = ''
    cls()
    for i in range(0,8):
        for j in range(0,8):
            l = level.get('leveldat')
            k = l[i][j]
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
        if i == 'q':
            playing = False
        if level['pal'][ level['leveldat'][p_y][p_x]] == 'enemy':
            if not bool(randint(0,4)):
                battle()

print('Bye Bye!')
