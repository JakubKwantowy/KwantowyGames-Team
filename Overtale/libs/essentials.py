def keyselect(up,down,key,current,inc,min,max):
    if key == up:
        if current < max:
            current += inc
        else:
            current = min
    elif key == down:
        if current > min:
            current -= inc
        else:
            current = max
    return current
    
def selectdisplay(element,selection):
        for i in range(0,len(element)):
            if i == selection:
                print('* '+element[i])
            else:
                print('  '+element[i])

def getcommandlist():
    import os
    if os.name == 'posix':
        return {
        'clear':'clear'
        }
    elif os.name == 'nt':
        return {
        'clear':'cls'
        }

def fileread(path):
    lines = []
    fobj = open(path, 'r')
    for line in fobj:
        appending = line.split('\n')
        lines.append(appending[0])
            
    fobj.close()
    return lines
    
def filewrite(path, content):
    fobj = open(path, 'w')
    for i in content:
        fobj.write(str(i)+'\n')
    fobj.close()