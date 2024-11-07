% 1)
movie(Movie, 2006).

% 2)
movie(Movie, Year), Year =< 2001.

% 3)
movie(Movie, Year), (Year = 2000; Year = 2006).

% 4)
movie(the_godfather_part_iii, Year), Year \= 1990.
