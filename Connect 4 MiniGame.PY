import random
import copy
import sys

BOARDHEIGHT = 6
BOARDWIDTH = 0

def main():
    playercount = 0

    logo()
    BOARDWIDTH = ask()
    num66=ask1()

    while True:
        humanTile, computerTile = enterHumanTile()
        turn = whoGoesFirst()
        print('%s will go first.' % (turn))
        mainBoard = getNewBoard(BOARDWIDTH)

        while True:
            if turn == 'Player':
                drawBoard(mainBoard,BOARDWIDTH)
                move = getHumanMove(mainBoard, BOARDWIDTH)
                makeMove(mainBoard, humanTile, move)
                playercount +=1
                if isWinner(mainBoard, humanTile, BOARDWIDTH):
                    winner = 'Player'
                    break
                turn = 'Computer'
            else:
                drawBoard(mainBoard,BOARDWIDTH)
                print('Computer is thinking...')
                move = getComputerMove(mainBoard, computerTile, num66, BOARDWIDTH)
                makeMove(mainBoard, computerTile, move)
                if isWinner(mainBoard, computerTile, BOARDWIDTH):
                    winner = 'Computer'
                    break
                turn = 'Player'

            if isBoardFull(mainBoard,BOARDWIDTH):
                winner = 'Draw~~'
                break

        drawBoard(mainBoard, BOARDWIDTH)
        print('Winner is %s' % winner)
        print('Total Player Attempt: %s' % playercount)
        totalAttempt(playercount)
        if playAgain():
            playercount = 0
            BOARDWIDTH = ask()
            num66=ask1()
        else :
            break


        
def totalAttempt(playercount):
    if playercount > 15:
        print('You Can Do Better~~~')
    elif playercount < 15:
        print('Not Too Bad~~~')
    elif playercount < 10:
        print('You Have The Talent~~~')



def playAgain():
    print('Do you want to play again? (y or n)')
    return input().lower().startswith('y')
    


def enterHumanTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']



def drawBoard(board, BOARDWIDTH):
    print()
    
    print(' ', end='')
    for x in range(1, BOARDWIDTH + 1):
        print('  %s   ' % x, end='')
    print()

    print('+-----+' + ('-----+' * (BOARDWIDTH - 1)))

    for y in range(BOARDHEIGHT):
        print('|     |' + ('     |' * (BOARDWIDTH - 1)))

        print('|', end='')
        for x in range(BOARDWIDTH):
            print('  %s  |' % board[x][y], end='')
        print()

        print('|     |' + ('     |' * (BOARDWIDTH - 1)))

        print('+-----+' + ('-----+' * (BOARDWIDTH - 1)))



def getNewBoard(BOARDWIDTH):
    board = []
    for x in range(BOARDWIDTH):
        board.append([' '] * BOARDHEIGHT)
    return board



def getHumanMove(board,BOARDWIDTH):
    while True:

        print('Pick a column to INSERT? (1-%s, or "q" to quit the game)' % (BOARDWIDTH))
        move = input()
        if move.lower().startswith('q'):
            sys.exit()
        if not move.isdigit():
            continue
        move = int(move) - 1
        if isValidMove(board, move, BOARDWIDTH):
            return move



def getComputerMove(board, computerTile, num66, BOARDWIDTH):
    potentialMoves = getPotentialMoves(board, computerTile, num66, BOARDWIDTH)
    bestMoveScore = max([potentialMoves[i] for i in range(BOARDWIDTH) if isValidMove(board, i, BOARDWIDTH)])
    bestMoves = []
    for i in range(len(potentialMoves)):
        if potentialMoves[i] == bestMoveScore:
            bestMoves.append(i)
    return random.choice(bestMoves)



def getPotentialMoves(board, playerTile, lookAhead, BOARDWIDTH):
    if lookAhead == 0:
        return [0] * BOARDWIDTH

    potentialMoves = []

    if playerTile == 'X':
        enemyTile = 'O'
    else:
        enemyTile = 'X'

    if isBoardFull(board, BOARDWIDTH):
        return [0] * BOARDWIDTH

    potentialMoves = [0] * BOARDWIDTH
    for playerMove in range(BOARDWIDTH):
        dupeBoard = copy.deepcopy(board)
        if not isValidMove(dupeBoard, playerMove,BOARDWIDTH):
            continue
        makeMove(dupeBoard, playerTile, playerMove)
        if isWinner(dupeBoard, playerTile, BOARDWIDTH):
            potentialMoves[playerMove] = 1
            break
        else:
            if isBoardFull(dupeBoard, BOARDWIDTH):
                potentialMoves[playerMove] = 0
            else:
                for enemyMove in range(BOARDWIDTH):
                    dupeBoard2 = copy.deepcopy(dupeBoard)
                    if not isValidMove(dupeBoard2, enemyMove, BOARDWIDTH):
                        continue
                    makeMove(dupeBoard2, enemyTile, enemyMove)
                    if isWinner(dupeBoard2, enemyTile, BOARDWIDTH):
                        potentialMoves[playerMove] = -1
                        break
                    else:
                        results = getPotentialMoves(dupeBoard2, playerTile, BOARDWIDTH, lookAhead - 1)
                        potentialMoves[playerMove] += (sum(results) / BOARDWIDTH) / BOARDWIDTH
    return potentialMoves



def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'Player'



def makeMove(board, player, column):
    for y in range(BOARDHEIGHT-1, -1, -1):
        if board[column][y] == ' ':
            board[column][y] = player
            return



def isValidMove(board, move,BOARDWIDTH):
    if move < 0 or move >= (BOARDWIDTH):
        return False

    if board[move][0] != ' ':
        return False

    return True



def isBoardFull(board,BOARDWIDTH):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == ' ':
                return False
    return True



def ask():
    print('\n\n\t\t\t\tMode 1_Normal 6x7\t\t\tMode 2_Advanced 6x9\t\t\tMode 3_Instruction\n\n\n')
    num66=10000
    
    while num66 > 2:
        BOARDWIDTH = int(input('Enter a Mode:'))
        if BOARDWIDTH == 1:
            BOARDWIDTH = 7
            num66=1
            return BOARDWIDTH
        elif BOARDWIDTH == 2:
            BOARDWIDTH = 9
            num66=1
            return BOARDWIDTH
        elif BOARDWIDTH == 3:
            print('\n\n\t\t1. Pick a GameMode that you interested.\n')
            print('\t\t2. Pick a Difficulty for the game.\n')
            print('\t\t3. Choose ‘X’ or ‘O’ to start the game.\n')
            print('\t\t4. You need to connect at least 4 discs to win a normal game and at least 5 dics to win an advanced game.\n')
            print('\t\t5. You can type ‘q’ if you wish to quit the game.\n')
            print('\t\t6. Type the number of column that you wish to insert the disc and the disc will automatically inserted to the bottom of the column.\n')
            print('\n')

    return BOARDWIDTH



def ask1():
    print('\n\n\t\t\t\t1_Easy\t\t\t2_Normal\t\t\t3_Hard\n\n\n')
    num2 = 1000000000

    while num2 > 3:
        num2 = int(input('Enter a Difficult:'))
        
    return num2-1



def logo():
    print("\n\n\n\n")
    print("\t\t\t============  ============  ===  =======    ===  =======    ============  ============  ===============       ==    ==")
    print("\t\t\t============  ============  === =========   === =========   ============  ============  ===============      ==     ==")
    print("\t\t\t===           ===      ===  ====       ===  ====       ===  ===           ===                 ===           ==      ==")
    print("\t\t\t===           ===      ===  ===        ===  ===        ===  =======       ===                 ===          ===========")
    print("\t\t\t===           ===      ===  ===        ===  ===        ===  =======       ===                 ===          ===========")
    print("\t\t\t===           ===      ===  ===        ===  ===        ===  ===           ===                 ===                   ==")
    print("\t\t\t============  ============  ===        ===  ===        ===  ============  ============        ===                   ==")
    print("\t\t\t============  ============  ===        ===  ===        ===  ============  ============        ===                   ==")
    print("\n")



def isWinner(board, tile, BOARDWIDTH):

    if BOARDWIDTH == 7:

        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True

        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True

        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        return False

    elif BOARDWIDTH == 9:

        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 4):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile and board[x+4][y] == tile:
                    return True

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 4):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile and board[x][y+4] == tile:
                    return True


        for x in range(BOARDWIDTH - 4):
            for y in range(3, BOARDHEIGHT):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile and board[x+4][y-4] == tile:
                    return True


        for x in range(BOARDWIDTH - 4):
            for y in range(BOARDHEIGHT - 4):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile and board[x+4][y+4] == tile:
                    return True

        return False






if __name__ == '__main__':
    main()
