tree_dotstring(T,S) :- nonvar(T), !, tree_dots_dl(T,L-[]), atom_chars(S,L). 
tree_dotstring(T,S) :- atom(S), atom_chars(S,L), tree_dots_dl(T,L-[]).

tree_dots_dl(nil,L1-L2) :- symbol('_',L1-L2).
tree_dots_dl(t(X,Left,Right),L1-L4) :- 
   letter(X,L1-L2),
   tree_dots_dl(Left,L2-L3),
   tree_dots_dl(Right,L3-L4).

symbol(X,[X|Xs]-Xs).

letter(X,L1-L2) :- symbol(X,L1-L2), char_type(X,alpha).

:- use_module(library(bounds)).

% Pss adalah list of lists papan permainan.

sudoku(Pss) :-
    flatten(Pss, Ps),
    Ps in 1..9,
    maplist(all_different, Pss),
    Pss = [R1,R2,R3,R4,R5,R6,R7,R8,R9],
    columns(R1, R2, R3, R4, R5, R6, R7, R8, R9),
    blocks(R1, R2, R3), blocks(R4, R5, R6), blocks(R7, R8, R9),
    label(Ps).

columns([], [], [], [], [], [], [], [], []).
columns([A|As],[B|Bs],[C|Cs],[D|Ds],[E|Es],[F|Fs],[G|Gs],[H|Hs],[I|Is]) :-
    all_different([A,B,C,D,E,F,G,H,I]),
    columns(As, Bs, Cs, Ds, Es, Fs, Gs, Hs, Is).

blocks([], [], []).
blocks([X1,X2,X3|R1], [X4,X5,X6|R2], [X7,X8,X9|R3]) :-
    all_different([X1,X2,X3,X4,X5,X6,X7,X8,X9]),
    blocks(R1, R2, R3).

