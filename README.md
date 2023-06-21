# WORDLE HELPER
#### Video Demo:  https://youtu.be/WCupjI6thLM
#### Description:

This project is a Wordle Helper, (you can check this game out here: https://www.nytimes.com/games/wordle/index.html). The goal of the game is to guess a correct 5 letter word with only 6 tries. it may seem difficult but after each guess we get some feedback about correctness of our guess (good letter on a good spot, good letter but wrong spot, and bad letter).

Maybe it was not the most practical project but I had some fun working on it and above all I practiced my **Python** skills.

First of all, I had to obtain a list of all (or at least of many) English 5 letter words, it was not hard, and soon enough I could read those words into my program. 

The next step was construction of user input. This part seemed problematic but I settled on an easy solution. That is, just inputting 5 letter words and a string of number correspodning with errors which Wordle gave you.

Program itself is quite simple, depending on the error, the list of words is narrowed down, if we know that the first letter is "a" we can exclude all of the words which do not have "a" on this position, similarily, if we have a letter "b" on a second position but we know that it is a good letter but in a wrong spot we can exclude all words with "b" on a second position and all words without "b" whatsoever. The same goes with wrong letter, all words containg them are excluded.

Witg this simple algorithm, a few functions and we can solve almost every Wordle puzzle. Moreover, player can still choose between different words, they are just a suggestion.

In this project I practiced: writing code using paradigms of functional programming, debugging, and writing tests.

Overall, I am quite happy with how it turned out, 

Thanks for your attention.