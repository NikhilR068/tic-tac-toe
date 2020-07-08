#Tic - Tac - Toe
#No packages used
 
b=[' ' for x in range(10)]

def insert(letter, pos):
    b[pos]=letter
def blank(pos):
    return b[pos]==' '
#Board Design

def boardprint(b):
    print('   |   |   ')
    print(' '+b[1]+' | '+b[2]+' | '+b[3]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+b[4]+' | '+b[5]+' | '+b[6]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+b[7]+' | '+b[8]+' | '+b[9]+' ')
    print('   |   |   ')
def winner(bo, le):
    return (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le)
    
#Player Move


def pmove():
    run=True
    while run:
        pos=input('select a position on board(1-9):')
        try:
            pos=int(pos)
            if pos>0 and pos<10:
                if blank(pos):
                    run=False
                    insert('X', pos)
                else:
                    print('space occupied')
                    pmove()
            else:
                print('type valu from 1 to 9')
                pmove()
        except:
            print('integer value only')
            pmove()

#Computer Move
    
def compmove():
    possiblemove=[x for x, letter in enumerate(b) if letter ==' ' and x!=0]
   
    move=0
    if 5 in possiblemove:
        move=5
        return move
    for le in ['O','X']:
        for i in possiblemove:
            bcopy=b[:]
            bcopy[i]=le
            if winner(bcopy, le):
                move=i
                return move
    edgesopen=[]
    for i in possiblemove:
        if i in (2,4,6,8):
            edgesopen.append(i)
    if len(edgesopen)>0:
        move=randomm(edgesopen)
        return move            
    corneropen=[]
    for i in possiblemove:
        if i in (1,3,7,9):
            corneropen.append(i)
    if len(corneropen)>0:
        move=randomm(corneropen)
        return move
    if 5 in possiblemove:
        move=5
        return move
    return move
        
    
def randomm(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def full(b):
    if b.count(' ')>1:
        return True
    else:
        return False    
    
            
                    
def main():
    print('Tic tac Toe')
    boardprint(b)
    
        
    while full(b):
        
        if not(winner(b,'O')):
            pmove()
            
        else:
            print('you lose')
            print('click enter to exit')
            j=input()
            break
        if b[1]==' ' and b[2]==' ' and b[3]==' ' and b[4]==' ' and b[6]==' ' and b[7]==' ' and b[8]==' ' and b[9]==' ' and b[5]=='X':
            l=[1,3,7,9]
            b[randomm(l)]='O'        
            boardprint(b)       
        elif not(winner(b, 'X')):
            move=compmove()
          
            if move==0:
                print('tie game')
                print('click enter to exit')
                j=input()
            else:
                insert('O',move)
                boardprint(b)
        else:
            print('you won')
            print('click enter to exit')
            j=input()
            break
    if full(b) and not(winner(b,'O')) and not(winner(b, 'X')):
        print('tie game')
        
    print('thank you for playing')
main()        
