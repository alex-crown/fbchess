# -*- coding: utf-8 -*-
import sys

gameover = ['wins', 'draw']
nonmovestrings = ['Starting', 'undo']
nonmovestrings.extend(gameover)

'''
wrapper around readline
lines returned are stripped
if no more input lines remain, prints results and quits
'''
def readnextline():
    line = input.readline()
    if not line:
        printresults('')
        print "quitting: no more input"
        quit()
    return line.strip()
    

'''
Reads a single move from the log
A move is of the form #. move or #... move
Reads game start, undos, and end
'''
def readmove():
    line = readnextline()
    while line != 'FBChess':
        line = readnextline()
    
    line = readnextline()
    if line != 'FBChess':
        return readmove()

    line = readnextline()
    if any([substring in line for substring in nonmovestrings]):
        return line
    
    # consume another line of input    
    readnextline()   
    
    # return this line which contains the move number, side, and move
    return readnextline()
    
'''
adds a single line of the form "movenum. move" to the list
. denotes a white move
... denotes a black move
'''
def addmovetolist(list, line):
    line = line.translate(None, '.')
    movenum, move = line.split(' ')
    movenum = int(movenum) - 1
    if movenum == len(list):
        list.append(move)
    else: # there was an undo or show
        list[movenum] = move

'''
outputs the algebraic notation for the game
'''
def printresults(move):
    # Print the results
    blacklen = len(black)
    for movenum in range(len(white)):
        print str(movenum + 1).ljust(4),
        print str(white[movenum]).ljust(8),
        if movenum < blacklen:
            print str(black[movenum]).ljust(8)
        else:
            print
    print move

# open files
numargs = len(sys.argv)
if numargs < 2:
    print 'missing input file'
    quit()

input = open(sys.argv[1])

if numargs == 3:
    output = open(sys.argv[2], 'w')
    sys.stdout = output


# create lists of moves for each side
white = []
black = []

# read in the first move
move = readmove()

# skip to the first move if "starting game" was selected
if not move.startswith("1"):
    move = readmove()

# read moves until end of game reached
while not any([string in move for string in gameover]):
    if "..." in move:
        addmovetolist(black, move)
    elif "." in move:
        addmovetolist(white, move)
    move = readmove()

printresults(move)
