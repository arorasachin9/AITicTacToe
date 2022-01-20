import random
class TicTacToe:
    def drawBoard(self,board):
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[7] + '|' + board[8] + '|' + board[9])


    def takeUserInput(self):
        letter=''
        while not(letter=='X' or letter=='O'):
            print("Do you want to be 'X' or 'O'?")
            letter = input().upper()

        if letter == 'X':
            return ['X','O']
        else:
            return ['O','X']


    def whoGoesFirst(self):
        if random.randint(0,1) == 0:
            return 'computer'
        else:
            return 'player'


    def playAgain(self):
        print('Do you want to play again? (Yes or No)')
        return input().lower().startswith('y')


    def nextMove(self,board, letter, move):
        board[move] = letter


    def isWinner(self,board,letter):
        return ((board[1]==letter and board[2]==letter and board[3]==letter) or
                (board[4]==letter and board[5]==letter and board[6]==letter) or
                (board[7]==letter and board[8]==letter and board[9]==letter) or
                (board[1]==letter and board[4]==letter and board[7]==letter) or
                (board[2]==letter and board[5]==letter and board[8]==letter) or
                (board[3]==letter and board[6]==letter and board[9]==letter) or
                (board[1]==letter and board[5]==letter and board[9]==letter) or
                (board[3]==letter and board[5]==letter and board[7]==letter))


    def getBoardCopy(self,board):
        dupBoard = []
        for i in board:
            dupBoard.append(i)
        return dupBoard


    def getPlayerMove(self,board):
        move = ''
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board[int(move)]==' ':
            if move not in '1 2 3 4 5 6 7 8 9'.split() or not board[int(move)]==' ':
                print("Invalid Move")
            print('What is your next move? (1-9)')
            move = input()
        return int(move)


    def chooseRandomMoveFromList(self,board, movesList):
        possibleMoves = []
        for i in movesList:
            if board[i]==' ':
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None


    def minimax(self,board, depth, isMax, alpha, beta, computerLetter):
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        if isWinner(board, computerLetter):
            return 10
        if isWinner(board, playerLetter):
            return -10
        if isBoardFull(board):
            return 0

        if isMax:
            best = -1000

            for i in range(1,10):
                if board[i]==' ':
                    board[i] = computerLetter
                    best = max(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) - depth)
                    alpha = max(alpha, best)
                    board[i] = ' '

                    if alpha >= beta:
                        break

            return best
        else:
            best = 1000

            for i in range(1,10):
                if board[i]==' ':
                    board[i] = playerLetter
                    best = min(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) + depth)
                    beta = min(beta, best)
                    board[i] = ' '

                    if alpha >= beta:
                        break

            return best


    def findBestMove(self,board, computerLetter):
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        bestVal = -1000
        bestMove = -1


        for i in range(1,10):
            if board[i]==' ':
                board[i] = computerLetter

                moveVal = minimax(board, 0, False, -1000, 1000, computerLetter)

                board[i] = ' '

                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal

        return bestMove


    def isBoardFull(self,board):
        for i in range(1,10):
            if board[i]==' ':
                return False
        return True

    def gameStart(self):
        print('\nWelcome to Tic Tac Toe!\n')
        print('Reference of numbering on the board')
        drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
        print('')

        while True:
            theBoard = [' '] * 10
            playerLetter, computerLetter = takeUserInput()
            turn = whoGoesFirst()
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    nextMove(theBoard, playerLetter, move)

                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print('You won the game')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie')
                            break
                        else:
                            turn = 'computer'
                else:
                    move = findBestMove(theBoard, computerLetter)
                    nextMove(theBoard, computerLetter, move)

                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print('You lose the game')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie')
                            break
                        else:
                            turn = 'player'
            if not playAgain():
                break
myOb = TicTacToe()
myOb.gameStart()