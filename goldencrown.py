kingdoms_emblems = {'Land':'Panda','Water':'Octopus','Ice':'Mammoth','Air':'Owl','Fire':'Dragon'}
ruler = 'None'
allies = ''
allies_count = 0

def main():
    global kingdoms_emblems
    global ruler
    global allies
    global allies_count

    inp = input().casefold().strip()
    if inp != '' and inp != None:
        if inp == "who is the ruler of southeros?":
            if allies_count >= 3:
                ruler = "King Shan"
            print(ruler)
        elif inp == 'allies of ruler?' or inp == 'allies of king shan?':
            if allies_count >= 3:
                print(allies.rstrip(', '))
            else:
                print('None')
        elif ',' in inp:
            s = inp.split(',')
            kingdom = s[0].strip()
            message = s[1].strip()[1:-1]  # remove "" from message
            ally = sendmessage(message, kingdom)
            if ally != '':
                allies += ally + ', '
                allies_count += 1
        else:
            print("Please enter a valid input")

def isembleminmessage(emblem,message):
    message = ''.join(sorted(''.join(message.split()))) #Sort alphabetically to reduce search time
    ecount = mcount = 0
    for c in emblem:
        ecount =  emblem.count(c)
        mcount = message.count(c)
        if mcount < ecount:
            return False
    return True

def sendmessage(message,kingdom):
    global kingdoms_emblems
    ally = ''
    kingdom = kingdom.capitalize()
    if kingdom in kingdoms_emblems.keys():
        if isembleminmessage(kingdoms_emblems[kingdom].casefold(),message):
            ally = kingdom
            kingdoms_emblems.pop(kingdom)

    return ally

if __name__ == '__main__':
    while(True):
        try:
            main()
        except Exception as e:
            print(e)
            break