
from pyswip.prolog import Prolog
from pyswip.easy import *
import sys

_ = 0
puzzle1 = [
            [_,_,6,_,3,_,9,5,_],
            [_,_,_,_,8,_,_,_,_],
            [_,_,_,_,_,2,_,1,8],
            [_,_,_,_,_,_,_,_,5],
            [_,_,1,4,2,5,6,_,_],
            [6,_,_,_,_,_,3,_,_],
            [1,6,_,2,_,_,_,_,_],
            [_,_,_,_,4,_,_,_,_],
            [_,2,7,_,6,1,4,_,_]
            ]


puzzle2 = [
            [1,_,_,_,8,_,6,_,4],
            [_,3,7,6,_,_,_,_,_],
            [5,_,_,_,_,_,_,_,_],
            [_,_,_,_,_,5,_,3,_],
            [_,_,6,_,1,_,8,_,_],
            [_,_,_,4,_,_,_,_,_],
            [_,_,_,_,_,_,_,_,3],
            [_,_,_,_,_,7,5,2,_],
            [8,_,2,_,9,_,7,_,_]
          ]


def cetak_papan(tabel):
    j=0
    for baris in tabel:
        if ((j % 3) == 0):
            print "".join(["|---", "----"*8, "|"])
        print "".join(["|", "|".join(" %s " % (i or " ") for i in baris), "|"])
        j=j+1
    print "".join(["|---", "----"*8, "|"])        

    
def cari_solusi(problem):
    prolog.consult("sudoku.pl")
    p = str(problem).replace("0", "_")
    hasil = list(prolog.query("L=%s,sudoku(L)" % p, maxresult=1))
    if hasil:
        hasil = hasil[0]
        return hasil["L"]
    else:
        return False

    
def main():

    print "---PROGRAM SUDOKU SOLVER---"
    print "INTEGRASI PROGRAM BAHASA PYTHON"
    print "DENGAN PROGRAM BAHASA PROLOG"
    print "--------------------------------"

    try:
        temp = input("lihat puzzle yang tersedia?")
    except (SyntaxError, TypeError, NameError) as e:
    	temp = None
    
    print
    print "-- PUZZLE YANG TERSEDIA --"
    print
    print "-- PUZZLE1 --"
    cetak_papan(puzzle1)    
    print

    print "-- PUZZLE2 --"
    cetak_papan(puzzle2)    
    print

    try:
        puzzle = input("pilih puzzle yang akan diselesaikan dengan input [puzzle1/puzzle2]")
        if ((puzzle != puzzle1) and (puzzle != puzzle2)):
            print("input tidak sesuai, program keluar...")
            sys.exit()
    except (SyntaxError, TypeError, NameError) as e:
    	print("input tidak sesuai, program keluar...")
    	sys.exit()

    print "-- PUZZLE --"
    cetak_papan(puzzle)    
    print
    print " -- SOLUSI --"
    solution = cari_solusi(puzzle)
    if solution:
        cetak_papan(solution)
    else:
        print "Puzzle tidak memiliki solusi"

        
if __name__ == "__main__":
    prolog = Prolog()
    main()
