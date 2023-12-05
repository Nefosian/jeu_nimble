from random import randint

def newBoard(n, p):
    '''
    fonction qui creer le plateau de jeu
    enter:
    n : int()
    p : int()
    '''
    return [randint(0,p) for i in range(n)]


def display(board,n):
    '''
    fonction qui fait l'affichage du jeu
    enter:
    board : lst()
    n : int()
    '''
    print('\nPlateau :\n')
    for elt in board:
        if elt>=10:
            print(elt, end="| ")
        else:
            print(elt, end=" | ")
    print(f"\n{(n*4-1)*'-'}")
    for i in range(n):
        if i+1>=10:
            print(i+1, end="| ")
        else:
            print(i+1, end=" | ")


def possibleSquare(board, n, i):
    '''
    fonction qui verifie si la case est vide et compris dans le tableau
    enter:
    board : lst()
    n : int()
    i : int()
    '''
    return n>=i>1 and board[i-1]>0


def selectSquare(board, n):
    '''
    fonction qui regarde si la case selectionner est valable
    enter:
    board : lst()
    n : int()
    '''
    while True:
        i=int(input("Choississez une case valable : "))
        if possibleSquare(board,n,i):
            return i
            

def possibleDestination(board, n, i, j):
    '''
    fonction qui retourne True si un pion peut aller de la case i a j 
    enter:
    board : lst()
    n : int()
    i : int()
    j : int()
    '''
    return n>=i>j>0 and board[i-1]>0


def selectDestination(board, n,i):
    '''
    fonction qui regarde si la case selectionner est valable
    enter:
    board : lst()
    n : int()
    i : int()
    '''
    while True:
        j=int(input("Choississez une case valable où aller : "))
        if possibleDestination(board,n,i,j):
            return j

 
def move(board, n, i, j):
    '''
    fonction qui fait bouger un pion de la case i a j
    enter:
    board : lst()
    n : int()
    i : int()
    j : int()
    '''
    board[i-1]-=1
    board[j-1]+=1
    
    
def lose(board, n):
    '''
    fonction qui verifie si la partieest terminer ou non et renvoie False si elle n'est pas terminer et True sinon
    enter:
    board : lst()
    n : int()
    '''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if possibleDestination(board,n,i,j):
                return False
    return True

        
def nimble(n, p):
    '''
    fonction qui s'occcupe de tout le déroulement du jeu avec n comme taille de plateau et p le nombre de pions voulu au max sur chaque case
    enter:
    n : int()
    p : int()
    '''
    plateau = newBoard(n, p)
    display(plateau, n)
    joueur = 1
    while not lose(plateau, n):
        print(f"\n\nC'est au tour du joueur {joueur} ")
        dep = selectSquare(plateau, n)
        dest = selectDestination(plateau, n, dep)
        move(plateau, n, dep, dest)
        display(plateau, n)
        if lose(plateau, n):
            return f"\n\nLe joueur {joueur} a gagné la partie. "
        joueur = 3 - joueur
        
        
print(nimble(6,3))
