# The 7 Wonders Treasure Hunt:

This is an interactive puzzle designed to assess the soft skills of a person. Questions in this treasure hunt game are related to 7 wonders of the world as the central theme is <b>The Seven Wonders of the World</b>. Though the user is not aware of the answer by seeing the question user will be having clues at each level and based on their soft skills such as eye detail, logical thinking, understanding, problem-solving, etc the user can solve the answers to the questions present in each level. 

# Website
users can click on this link and play the game
## http://elitmusproj.pythonanywhere.com/

#### User login
User can signup with the help of their email id and have fun playing the game 

#### Admin login
username: admin<br>
password: admin

## Answers to the questions:
1. 13000
2. RoseCity
3. 600
4. ----
5. Quechua
6. 365
7. 	travertine limestonE
8. 	Yamuna

## How to play
To start the game, you need to sign in with your email account. Firstly, user will get a letter saying to complete all levels to meet another treasurer friend. Then, user will have to solve the riddles and get to the final/result page successfully.<br>
The goal of the game is to solve all the levels and pass all the seven wonders. At certain levels, you have to solve the riddle in the given chances else if you choose the wrong option and if no chances are left, the game will be over and user need to restart the game. User can use hints/clues to answer the riddles. You can use the clue button to get the clue for the riddle. At the end of the game, user will be meeting the friend finally from whom user received the letter<br>
The game ends when user reach a dead end. At the final step, the score will be shown to you. In any step, if you reach a dead end, you will be redirected to the starting page.

## Soft Skills to be assessed:
Based on user's ability to solve at each level, their various soft skills can be assessed. Some of them are 
1. Problem-Solving - The game requires players to solve puzzles and find ways to complete the game, which can help develop their problem-solving skills. By figuring out the best way to navigate through the jungle and find solutions, players can enhance their critical thinking skills. 
2. Eye for detail - Players need to pay close attention to the details in the game to complete successfully.
3. logical thinking - The players should have the ability to reason, analyze, and make decisions based on facts, evidence, and sound reasoning.
4. Understanding - Sometimes the player need to understand the game more effectively to complete in less time.

## Information about the Game:
There are a total of 8 levels of which 7 levels are the questions related to the 7 wonders and to get some relief or fun, one level is added extra in the middle. Whenever the user solves a question they will be redirected to another page showing another wonder of the world. There are 3 dead ends in the game in which out of given chances if they are unable to solve and give the correct answer the user may go out of the loop asking to re-start the game. By playing this treasure hunt game users not only will have fun but also will be knowing more general knowledge about the 7 wonders of the world.

## Technologies used:
I used the Django rest framework to complete this project and it includes HTML, Python, CSS, and some JavaScript wherever required. I used HTML, CSS, and JavaScript for user view in a good way and Django, Python files to integrate and store and display the data that the user has given for the question level wise.

## Steps to set up the project:
Type the following command to install virtualenvwrapper so that we can create virtual environment.<br>
### `pip install virtualenvwrapper-win` <br>
next do the following command to create a new virtual environment for the project<br>
### `mkvirtualenv env`
Here env is the name of the virtual environment and it can be any name of our interest, by default we will be entered into the virtual environment that we had created and
whenever you want to go to the created environment you can easily go by using the below command
workon "virtual environment name"<br>
### `workon env`
check if the system has django installed or not, if django is not present install django in the virtual environment where so that django of current version will be installed in that environment and when you want to do another project of different djnago version you can do that in another environment and that is the use of creating virtual environments<br>
to check<br>
### `python -m django --version`<br>
to install django<br>
### `pip install django`<br>
Create a new folder to store the project <br>
mkdir "project name"<br>
### `mkdir puzzle`<br>
go to the directory<br>
### `cd puzzle`<br>
To set up the project simply download the files from gitHub. After downloading the files open command prompt in the location of the folder you created and type the following command to run the project that you had created<br>
### `python manage.py runserver`<br>

## Features List
Anyone with an email address can create an Id and password to participate in the game<br>
8 levels along with clues for each level<br>
3 deadends (level 3,4 and 7 are dead ends)<br>
Minimum 1 solution<br>
All the progress/user data (with their answers and score they got out of total) is displayed as a table<br>
On refreshing, from either browser or website, the puzzle will restart from that level<br>
A dashboard for the admin on the admin side where user can see who all has played

