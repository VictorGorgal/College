% Respostas:
% resultado(joao, X).
% falta(X, Y), Y > 0.
% reprovado(jose).

% Fatos
resultado(joao, 8).
resultado(maria, 7).
resultado(pedro, 5).
resultado(jose, 6).
resultado(ana, 9).
falta(joao, 2).
falta(maria, 0).
falta(pedro, 5).
falta(jose, 1).
falta(ana, 0).

reprovado(X) :- 
    resultado(X, Nota), 
    falta(X, F), 
    (Nota < 6 ; F > 3).

aprovado(X) :- 
    resultado(X, Nota), 
    falta(X, F), 
    Nota > 6, 
    F < 2.
    
:- initialization(main).

main :-
    resultado(X, Nota),
    write(X), write(' - Nota: '), write(Nota), nl,
    fail.  
main.  
