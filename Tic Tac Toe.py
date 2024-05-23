# -*- coding: utf-8 -*-

def print_board(mat):
    print("    0    1    2")
    print(" *----*----*----*")
    for i in range(len(mat)):
        print("%d|"%i,end="")
        for j in range(len(mat)):
            print(" %2s |"%mat[i][j], end ="")
        print()
        print(" *----*----*----*")
        
def is_valid(mat,r,c):
    return mat[r][c]==''

def o(mat,p2):
    print("Enter valid locatin!")
    r,c =eval(input("%s enter location: "%p2))  
    while not is_valid(mat, r, c):
        print("Enter valid locatin!")
        r,c =eval(input("%s enter location: "%p2)) 
    mat[r][c]='O'
    return True
def x(mat,p1):
    print("Enter valid locatin!")
    r,c =eval(input("%s enter location: "%p1))  
    while not is_valid(mat, r, c):
        print("Enter valid locatin!")
        r,c =eval(input("%s enter location: "%p1))
    mat[r][c]='X'
    return True

def is_tie(mat):
    if count(mat)==9:
        return True
    return False
def win_check(mat,r,c):
    if r!=c and (r+c)!=2:
        if r == 1:
            if mat[r][c]==mat[r+1][c]==mat[r-1][c]!='' or (c==0 and mat[r][c]==mat[r][c+1]==mat[r][c+2]!='') or (c==2 and mat[r][c]==mat[r][c-1]==mat[r][c-2]!=''):
                return True
        if c==1:
            if mat[r][c]==mat[r][c+1]==mat[r][c-1]!=''or (r==0 and mat[r][c]==mat[r+1][c]==mat[r+2][c]!='') or (r==2 and mat[r][c]==mat[r-1][c]==mat[r-2][c]!=''):
                return True
    elif r==0:
        if c==0:
            if mat[r][c]==mat[r+1][c]==mat[r+2][c]!='' or mat[r][c]==mat[r][c+1]==mat[r][c+2]!='' or mat[r][c]==mat[r+1][c+1]==mat[r+2][c+2]!='':
                return True
        if c==2:
            if mat[r][c]==mat[r+1][c]==mat[r+2][c]!='' or mat[r][c]==mat[r][c-1]==mat[r][c-2]!='' or mat[r][c]==mat[r-1][c-1]==mat[r-2][c-2]!='':
                return True
    elif r==2:
        if c==0:
            if mat[r][c]==mat[r-1][c]==mat[r-2][c]!='' or mat[r][c]==mat[r][c+1]==mat[r][c+2]!='' or mat[r][c]==mat[r-1][c+1]==mat[r-2][c+2]!='':
                return True
        if c==2:
            if mat[r][c]==mat[r-1][c]==mat[r-2][c]!='' or mat[r][c]==mat[r][c-1]==mat[r][c-2]!='' or mat[r][c]==mat[r-1][c-1]==mat[r-2][c-2]!='':
                return True
    elif mat[r][c]==mat[r-1][c-1]==mat[r+1][c+1]!='' or mat[r][c]==mat[r+1][c-1]==mat[r-1][c+1]!='' or mat[r][c]==mat[r+1][c]==mat[r-1][c]!='' or mat[r][c]==mat[r][c+1]==mat[r][c-1]!='':
        return True
    return False
def count(mat):
    count=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]=='X' or mat[i][j]=='O':
                count +=1
    return count
            
def main():
    print("Ready To Play?\n'Tic Tac Toe'")
    play='y'
    p1 = input("\nEnter player 1 name: ")
    p2 = input("Enter player 2 name: ")
    cnt=[0,0]
    while( play!='n')&(play!='N'):
        mat=[['','',''],['','',''],['','','']]
        gameOver = False
        print("\n%s is 'X' and %s is 'O' ..."%(p1,p2))
        print_board(mat)
        r,c =eval(input("%s enter position: "%p1))
        mat[r][c]='X'
        while gameOver!=True:
            print_board(mat)
            r,c =eval(input("%s enter location: "%p2))     
            if is_valid(mat, r, c):
                mat[r][c]='O'
                print_board(mat)
            else:
                o(mat, p2)
                print_board(mat)
            if is_tie(mat)==True:
                print("TIE!")
                break
            if win_check(mat,r,c):
                gameOver=True
                print_board(mat)
                print("%s is the winner!!!"%p2)
                cnt[1]+=1
                break
            r,c =eval(input("%s enter location: "%p1))
            if is_valid(mat, r, c):
                mat[r][c]='X'
                print_board(mat)
            else:
                x(mat, p1)
                print_board(mat)
            if is_tie(mat)==True:
                print("TIE!")
                break
            if win_check(mat,r,c):
                gameOver=True
                print_board(mat)
                print("%s is the winner!!!"%p1)
                cnt[0]+=1
                break
        print("\n%d-%d -> %s-%s" % (cnt[0],cnt[1],p1,p2))
        print("\nPress 'y' for another game and 'n' to quit.")
        play = input("(y/n):")
        p1,p2=p2,p1
        cnt[0],cnt[1]=cnt[1],cnt[0]
    print("\nWell Played!")
main()
            