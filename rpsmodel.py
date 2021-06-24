from random import randint

def randomgame():
    OUTCOMES[(randint(ROCK, SCISSORS), randint(ROCK, SCISSORS))]()

def 

def incP1():
    global P1P
    P1P += 1

def incP2():
    global P2P
    P2P += 1

def getP1P():
    return P1P

def getP2P():
    return P2P

def dummy():
   pass

def pcs():
    print(f"P1: {P1P}\nP2: {P2P}")

def reset():
    global P1P, P2P
    P1P, P2P = 0, 0

ROCK = 1
PAPER = 2
SCISSORS = 3
P1, P1P = 1, 0
P2, P2P = 2, 0
OUTCOMES = {
    (ROCK, PAPER):incP2,
    (ROCK, SCISSORS):incP1,
    (PAPER, ROCK):incP1,
    (PAPER, SCISSORS):incP2,
    (SCISSORS, PAPER):incP1,
    (SCISSORS, ROCK):incP2, 
    (ROCK, ROCK):dummy,
    (PAPER, PAPER):dummy,
    (SCISSORS, SCISSORS):dummy
}
