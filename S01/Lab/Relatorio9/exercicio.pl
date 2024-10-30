resultado(joao, 3).
resultado(maria, 1).
resultado(ana, 4).
resultado(pedro, 4).
resultado(jose, 5).
falta(joao, 2).
falta(maria, 0).
falta(ana, 1).
falta(pedro, 2).
falta(jose, 5).

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
