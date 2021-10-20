# wheel_of_cheating
You better win any game of Hangman/Wheel Of Fortune based on videogames with this.

Run wheel_of.py as a script to use. Every time you want to try a different phrase combination, you need to type two lines, the current state of the "board," and the guessed letters (including nothing).

Will convert a string into a regex string which can be used to search through other strings to try and find a match as a possible solution to the hangman board.
In particular, converts "_" (underscores) into a variable character (which excludes all guessed letters), and all other characters into said character. Ignores case.

Currently compares the given board to every line in listOfItems.txt, which contains ~8000 unique videogames. Lists every phrase that matches the board (which includes substrings of full words within each line), and also lists the most common characters within those phrases.

Will continually loop for new inputs until the empty string is entered as the board (first input after recieving output).
