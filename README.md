# COMP9001_Final_Hyan0971

Game README

# Overview
This is a console-based puzzle game implemented in Python. The game has two levels:
-	Level 1: Push-the-box, where you move a box (o) onto the exit (E).
-	Level 2: Binary Password Lock puzzle, you need to explore a map, find hint mark (?), answer True/False questions, and then enter the correct password at the exit to win.
# Features
-	The map layout is chosen randomly in each game.
-	ASCII-art rendering in the console.
-	Box pushing physics (can’t	 push through walls or other boxes).
-	Interactive True/False quiz in the map.
-	Password verification based on quiz answers.
-	Restart or quit at any time.
# Usage
Run the game from the command line:
python game.py

When game started, use the following keys:
-	W: Move up
-	A: Move left
-	S: Move down
-	D: Move right
-	R: Restart current level
-	Q: Quit the game

# Gameplay Details
Level 1: Push the Box
-	Your character is represented by P, the box is represented by o, walls are represented by #, and the exit is represented by E.
-	Move next to the box and push it onto the exit. The exit is too high so you need a box to boost yourself up.
-	If you push the box into the exit, Level 1 is completed.
Level 2: Binary Password Lock
-	Explore the map to find hint mark ?.
-	Step in ‘?’ will trigger the question.
-	Each question corresponds to one bit: T = 1, F = 0.
-	Collect the correct bits (based on standard answers) in state['correct_bits'].
-	When you reach the exit (E), you will be prompted to enter the password.
-	Enter the right password to complete Level 2 and win the game.
# Customization
-	Maps: Add or modify layouts in maps.py under LEVEL1_MAPS and LEVEL2_MAPS.
-	Questions: Update question pools in question.py (format: (prompt, "T"/"F")).




