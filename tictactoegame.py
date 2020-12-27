field= ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def insertLetter(letter, position):
    field[position] = letter

def spaceIsFree(position):
    return field[position] == ' '
    
def printField(field):
    print("\033[4m"+field[1]+"|"+field[2]+"|"+field[3]+"\n"+field[4]+"|"+field[5]+"|"+field[6]+"\n\033[0m"+field[7]+"|"+field[8]+"|"+field[9])

    
def isWinner(fi, le):
    return (fi[7] == le and fi[8] == le and fi[9] == le) or (fi[4] == le and fi[5] == le and fi[6] == le) or (fi[1] == le and fi[2] == le and fi[3] == le) or (fi[1] == le and fi[4] == le and fi[7] == le) or (fi[2] == le and fi[5] == le and fi[8] == le) or (fi[3] == le and fi[6] == le and fi[9] == le) or (fi[1] == le and fi[5] == le and fi[9] == le) or (fi[3] == le and fi[5] == le and fi[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(field) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            fieldCopy = field[:]
            fieldCopy[i] = let
            if isWinner(fieldCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isFieldFull(field):
    if field.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printField(field)

    while not(isFieldFull(field)):
        if not(isWinner(field, 'O')):
            playerMove()
            printField(field)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(field, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printField(field)
        else:
            print('X\'s won this time! Good Job!')
            break

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        field = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

    
