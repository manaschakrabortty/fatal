# Snake game is one of the most popular arcade games of all time. In this game, the main objective of the player is to catch the maximum number of fruits without hitting the wall or itself. Creating a snake game can be taken as a challenge while learning Python or Pygame. It is one of the best beginner-friendly projects that every novice programmer should take as a challenge. Learning to build a video game is kinda interesting and fun learning. 

# We will be using Pygame to create this snake game. Pygame is an open-source library that is designed for making video games. It has inbuilt graphics and sound libraries. It is also beginner-friendly, and cross-platform. 

# Installation:
# To install Pygame, you need to open up your terminal or command prompt and type the following command:

# pip install pygame
# After installing Pygame we are ready to create our cool snake game.

# A step-by-step approach for creating a Snake Game using Pygame:
# Step 1: First we are importing the necessary libraries.

# After that, we are defining the width and height of the window in which the game will be played.
# And define the color in RGB format that we are going to use in our game for displaying text.
# # importing libraries
# import pygame
# import time
# import random
 
# snake_speed = 15
 
# # Window size
# window_x = 720
# window_y = 480
 
# # defining colors
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
 
#  Step 2: After importing libraries we need to initialize Pygame using pygame.init() method. 

# Create a game window using the width and height defined in the previous step.
# Here pygame.time.Clock() will be used further in the main logic of the game to change the speed of the snake.
# # Initialising pygame
# pygame.init()
 
# # Initialise game window
# pygame.display.set_caption('GeeksforGeeks Snakes')
# game_window = pygame.display.set_mode((window_x, window_y))
 
# # FPS (frames per second) controller
# fps = pygame.time.Clock()
 
#  Step 3: Initialize snake position and its size.

# After initializing snake position, initialize the fruit position randomly anywhere in the defined height and width.
# By setting direction to RIGHT we ensure that, whenever a user runs the program/game, the snake must move right to the screen.
# # defining snake default position 
# snake_position = [100, 50]
 
# # defining first 4 blocks of snake
# # body
# snake_body = [  [100, 50],
#                 [90, 50],
#                 [80, 50],
#                 [70, 50]
#             ]
# # fruit position 
# fruit_position = [random.randrange(1, (window_x//10)) * 10,
#                   random.randrange(1, (window_y//10)) * 10]
# fruit_spawn = True
 
# # setting default snake direction 
# # towards right
# direction = 'RIGHT'
# change_to = direction
 
# Step 4: Create a function to display the score of the player. 

# In this function, firstly we’re creating a font object i.e. the font color will go here.
# Then we are using render to create a background surface that we are going to change whenever our score updates.
# Create a rectangular object for the text surface object (where text will be refreshed)
# Then, we are displaying our score using blit. blit takes two argument screen.blit(background,(x,y))
# # initial score
# score = 0
 
# # displaying Score function
# def show_score(choice, color, font, size):
   
#     # creating font object score_font 
#     score_font = pygame.font.SysFont(font, size)
     
#     # create the display surface object
#     # score_surface
#     score_surface = score_font.render('Score : ' + str(score), True, color)
     
#     # create a rectangular object for the 
#     # text surface object
#     score_rect = score_surface.get_rect()
     
#     # displaying text
#     game_window.blit(score_surface, score_rect)
 
# Step 5: Now create a game over function that will represent the score after the snake is hit by a wall or itself. 

# In the first line, we are creating a font object to display scores.
# Then we are creating text surfaces to render scores.
# After that, we are setting the position of the text in the middle of the playable area.
# Display the scores using blit and updating the score by updating the surface using flip().
# We are using sleep(2) to wait for 2 seconds before closing the window using quit().
# # game over function
# def game_over():
   
#     # creating font object my_font
#     my_font = pygame.font.SysFont('times new roman', 50)
     
#     # creating a text surface on which text 
#     # will be drawn
#     game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
     
#     # create a rectangular object for the text
#     # surface object
#     game_over_rect = game_over_surface.get_rect()
     
#     # setting position of the text
#     game_over_rect.midtop = (window_x/2, window_y/4)
     
#     # blit will draw the text on screen
#     game_window.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
     
#     # after 2 seconds we will quit the 
#     # program
#     time.sleep(2)
     
#     # deactivating pygame library
#     pygame.quit()
     
#     # quit the program
#     quit()
# Step 6: Now we will be creating our main function that will do the following things:

# We will be validating the keys that will be responsible for the movement of the snake, then we will be creating a special condition that the snake should not be allowed to move in the opposite direction instantaneously.
# After that, if snake and fruit collide we will be incrementing the score by 10 and new fruit will be spanned.
# After that, we are checking that is the snake hit with a wall or not. If a snake hits a wall we will call game over function.
# If the snake hits itself, the game over function will be called.
# And in the end, we will be displaying the scores using the show_score function created earlier.
# # Main Function
# while True:
   
#     # handling key events
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 change_to = 'UP'
#             if event.key == pygame.K_DOWN:
#                 change_to = 'DOWN'
#             if event.key == pygame.K_LEFT:
#                 change_to = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 change_to = 'RIGHT'
 
#     # If two keys pressed simultaneously 
#     # we don't want snake to move into two directions
#     # simultaneously
#     if change_to == 'UP' and direction != 'DOWN':
#         direction = 'UP'
#     if change_to == 'DOWN' and direction != 'UP':
#         direction = 'DOWN'
#     if change_to == 'LEFT' and direction != 'RIGHT':
#         direction = 'LEFT'
#     if change_to == 'RIGHT' and direction != 'LEFT':
#         direction = 'RIGHT'
 
#     # Moving the snake
#     if direction == 'UP':
#         snake_position[1] -= 10
#     if direction == 'DOWN':
#         snake_position[1] += 10
#     if direction == 'LEFT':
#         snake_position[0] -= 10
#     if direction == 'RIGHT':
#         snake_position[0] += 10
 
#     # Snake body growing mechanism 
#     # if fruits and snakes collide then scores will be 
#     # incremented by 10
#     snake_body.insert(0, list(snake_position))
#     if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
#         score += 10
#         fruit_spawn = False
#     else:
#         snake_body.pop()
         
#     if not fruit_spawn:
#         fruit_position = [random.randrange(1, (window_x//10)) * 10, 
#                           random.randrange(1, (window_y//10)) * 10]
         
#     fruit_spawn = True
#     game_window.fill(black)
     
#     for pos in snake_body:
#         pygame.draw.rect(game_window, green, pygame.Rect(
#           pos[0], pos[1], 10, 10))
         
#     pygame.draw.rect(game_window, white, pygame.Rect(
#       fruit_position[0], fruit_position[1], 10, 10))
 
#     # Game Over conditions
#     if snake_position[0] < 0 or snake_position[0] > window_x-10:
#         game_over()
#     if snake_position[1] < 0 or snake_position[1] > window_y-10:
#         game_over()
     
#     # Touching the snake body
#     for block in snake_body[1:]:
#         if snake_position[0] == block[0] and snake_position[1] == block[1]:
#             game_over()
     
#     # displaying score continuously
#     show_score(1, white, 'times new roman', 20)
     
#     # Refresh game screen
#     pygame.display.update()
 
#     # Frame Per Second /Refresh Rate
#     fps.tick(snake_speed)
 
# Below is the Implementation 

# # importing libraries
# import pygame
# import time
# import random
 
# snake_speed = 15
 
# # Window size
# window_x = 720
# window_y = 480
 
# # defining colors
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
 
# # Initialising pygame
# pygame.init()
 
# # Initialise game window
# pygame.display.set_caption('GeeksforGeeks Snakes')
# game_window = pygame.display.set_mode((window_x, window_y))
 
# # FPS (frames per second) controller
# fps = pygame.time.Clock()
 
# # defining snake default position
# snake_position = [100, 50]
 
# # defining first 4 blocks of snake body
# snake_body = [[100, 50],
#               [90, 50],
#               [80, 50],
#               [70, 50]
#               ]
# # fruit position
# fruit_position = [random.randrange(1, (window_x//10)) * 10, 
#                   random.randrange(1, (window_y//10)) * 10]
 
# fruit_spawn = True
 
# # setting default snake direction towards
# # right
# direction = 'RIGHT'
# change_to = direction
 
# # initial score
# score = 0
 
# # displaying Score function
# def show_score(choice, color, font, size):
   
#     # creating font object score_font
#     score_font = pygame.font.SysFont(font, size)
     
#     # create the display surface object 
#     # score_surface
#     score_surface = score_font.render('Score : ' + str(score), True, color)
     
#     # create a rectangular object for the text
#     # surface object
#     score_rect = score_surface.get_rect()
     
#     # displaying text
#     game_window.blit(score_surface, score_rect)
 
# # game over function
# def game_over():
   
#     # creating font object my_font
#     my_font = pygame.font.SysFont('times new roman', 50)
     
#     # creating a text surface on which text 
#     # will be drawn
#     game_over_surface = my_font.render(
#         'Your Score is : ' + str(score), True, red)
     
#     # create a rectangular object for the text 
#     # surface object
#     game_over_rect = game_over_surface.get_rect()
     
#     # setting position of the text
#     game_over_rect.midtop = (window_x/2, window_y/4)
     
#     # blit will draw the text on screen
#     game_window.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
     
#     # after 2 seconds we will quit the program
#     time.sleep(2)
     
#     # deactivating pygame library
#     pygame.quit()
     
#     # quit the program
#     quit()
 
 
# # Main Function
# while True:
     
#     # handling key events
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 change_to = 'UP'
#             if event.key == pygame.K_DOWN:
#                 change_to = 'DOWN'
#             if event.key == pygame.K_LEFT:
#                 change_to = 'LEFT'
#             if event.key == pygame.K_RIGHT:
#                 change_to = 'RIGHT'
 
#     # If two keys pressed simultaneously
#     # we don't want snake to move into two 
#     # directions simultaneously
#     if change_to == 'UP' and direction != 'DOWN':
#         direction = 'UP'
#     if change_to == 'DOWN' and direction != 'UP':
#         direction = 'DOWN'
#     if change_to == 'LEFT' and direction != 'RIGHT':
#         direction = 'LEFT'
#     if change_to == 'RIGHT' and direction != 'LEFT':
#         direction = 'RIGHT'
 
#     # Moving the snake
#     if direction == 'UP':
#         snake_position[1] -= 10
#     if direction == 'DOWN':
#         snake_position[1] += 10
#     if direction == 'LEFT':
#         snake_position[0] -= 10
#     if direction == 'RIGHT':
#         snake_position[0] += 10
 
#     # Snake body growing mechanism
#     # if fruits and snakes collide then scores
#     # will be incremented by 10
#     snake_body.insert(0, list(snake_position))
#     if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
#         score += 10
#         fruit_spawn = False
#     else:
#         snake_body.pop()
         
#     if not fruit_spawn:
#         fruit_position = [random.randrange(1, (window_x//10)) * 10, 
#                           random.randrange(1, (window_y//10)) * 10]
         
#     fruit_spawn = True
#     game_window.fill(black)
     
#     for pos in snake_body:
#         pygame.draw.rect(game_window, green,
#                          pygame.Rect(pos[0], pos[1], 10, 10))
#     pygame.draw.rect(game_window, white, pygame.Rect(
#         fruit_position[0], fruit_position[1], 10, 10))
 
#     # Game Over conditions
#     if snake_position[0] < 0 or snake_position[0] > window_x-10:
#         game_over()
#     if snake_position[1] < 0 or snake_position[1] > window_y-10:
#         game_over()
 
#     # Touching the snake body
#     for block in snake_body[1:]:
#         if snake_position[0] == block[0] and snake_position[1] == block[1]:
#             game_over()
 
#     # displaying score continuously
#     show_score(1, white, 'times new roman', 20)
 
#     # Refresh game screen
#     pygame.display.update()
 
#     # Frame Per Second /Refresh Rate
#     fps.tick(snake_speed)
# Output:


# Snake using Pygame

# Code Explanation:

# The code starts by importing the necessary libraries.
# These are pygame, time, and random.
# Next, the code defines some variables.
# The snake_speed variable controls how fast the snake moves around the screen.
# The window_x and window_y variables define the size of the game window onscreen.
# The next line of code initializes pygame.
# This is important because it sets up all of the game objects and their properties so that they can be used later in the program.
# Next, the code creates an instance of pygame’s GameWindow class object.
# This object represents a rectangular area onscreen that can be filled with graphics and text content.
# The GameWindow object has two properties: width and height .
# These values represent how wide and tall the game window is respectively.
# The next line of code assigns values to these properties based on a user-defined value called snake_speed .
# This variable tellspygame how fast (in pixels per second) to move the snake aroundthe screen.
# Higher values will make for faster movement but also more intense gameplay!
# Next, PyGame starts loading various images into memory to use as background graphics for our game world .
# First it loads in an
# The code will create a window with dimensions of 720×480 pixels.
# The colours black, white, red, green and blue will be used to represent the game’s various elements.
# Next, the pygame module will be imported and initialized.
# This will allow us to start working with the game’s various objects and functions.
# The game’s main loop will then be started by calling pygame.init().
# This function will ensure that all of the necessary modules are loaded and ready for use.
# Finally, we’ll call the window’s constructor to create our game window.
# The code starts by creating a pygame.display.set_mode() function to set the window size and position.
# The code then creates a game window and sets its mode to (0, 0).
# Next, the code defines some variables: fps, snake_position, snake_body, and fruit_position.
# These variables will be used to control the speed of the snake, where it starts from (snake_position), how wide it is (snake_body), where the fruit is located (fruit_position), and whether or not fruit should spawn (fruit_spawn).
# The next block of code calculates the distance between each point on the screen using pygame.time.Clock().
# This allows us to move the snake around on-screen without having to constantly recalculate its position.
# Finally, we set up two boolean variables: fruit_spawn and analyze().
# These will determine whether or not fruit will spawn at random locations on-screen and be analyzed for player input.
# The code sets up a basic game window with a snake positioned at (100, 50) on the X-axis and (window_x, window_y) on the Y-axis.
# The FPS controller is initialized and set to run at 60 frames per second.
# The next block of code defines the body of the snake.
# A list of ten [100, 50] points is created, starting at position (100, 50).
# The first four points are set to be in the center of the snake’s body while the remaining six points are evenly spaced around it.
# Next, a fruit position is defined as [(random.randrange(1, (window_x//10)) * 10), (random.randrange(1
# The code starts by initializing some variables.
# The first is the score, which starts at 0.
# The second is the direction variable, which will determine how the snake moves.
# The show_score() function is called whenever a player makes a choice.
# This function contains three parts: creating a font object, creating a display surface object, and displaying text on the display surface.
# First, the score_font object is created.
# This object stores information about the font used to display text on the screen (in this case, Times New Roman).
# Next, the score_surface object is created and initialized with information about the font and size of text that will be displayed (50 points in size).
# Finally, using blit(), the score_rect object is copied onto the score_surface object so that it can be displayed onscreen.
# The game_over() function ends any current game play and terminates Python code running in this module (assuming no other functions call it).
# First, an instance of SysFont named my_font is created.
# Then 50 points in size for Times New Roman are specified as its typeface and color values.
# Finally, game over() is called to end all game play and terminate Python code running in
# The code first initializes some variables, including the score variable.
# The code then creates a function called show_score().
# This function will be used to display the current score on the screen.
# The show_score() function first creates a font object called score_font and sets its size to 50 points.
# Next, the function creates a display surface object called score_surface and sets its color to white.
# Finally, the show_score() function blits the score_surface object onto the game window’s screen.
# The game over() function is responsible for cleaning up resources after the game has ended.
# First, it creates a font object called my_font and sets its size to 20 points.
# Then, the game over() function bl
# The code first creates a text surface object called game_over_surface.
# The text will be rendered in the font my_font and the color red.
# Next, a rectangular object is created for the text surface object.
# This object will have its midpoint at (window_x/2, window_y/4).
# Finally, position of the text on the rectangle is set using game_over_rect.midtop().
# The code creates a text surface object called game_over_surface.
# This object will be used to display the player’s score and the message “Your Score is :”.
# Next, a rectangular object called game_over_rect is created.
# This object will be used to position the text on the surface.
# The midpoint of the rectangle is set to (window_x/2, window_y/4).
# The code starts by initializing the pygame library.
# Next, the code creates a window and assigns it to game_window.
# The window has a surface (a graphic representation of the screen) and a Rectangle object that specifies its size and position.
# Next, the code blits (transfers) the text “GAME OVER” onto the game_over_surface object.
# The text is drawn in white, centered on top of the game_over_rect object.
# The program then sets up a timer that will run for 2 seconds.
# At this point, the program will quit because there is no more code to execute.
# The code will check for key events and if the event corresponds to a valid key, it will change the text displayed on screen accordingly.
# If you press any other key, the program will continue to run as normal.
# The code starts by checking to see if the player has pressed two keys at the same time.
# If they have, the code changes the direction of the snake.
# Next, the code checks to see if either key was pressed in a different direction than expected.
# If it was, then the code adjusts the position of the snake accordingly.
# Finally, it updates how big the snake’s body is getting.
# The code will check if the two keys being pressed at the same time are either ‘UP’ or ‘DOWN’.
# If they are, then the direction of the snake will be changed accordingly.
# If the two keys being pressed are not equal, then the code will check to see if they are different directions.
# If they are not, then the snake’s position will be adjusted by 10 pixels in each direction.
# Lastly, a function is created that will change how big the snake’s body grows when it moves.
# The code starts by creating a list of snake positions.
# The first position in the list is at (0, 0), and the last position in the list is at (window_x-10, window_y-10).
# Next, the code checks to see if any of the positions in the snake are equal to a fruit position.
# If so, then that fruit gets scored 10 points and is added to the fruit spawn variable.
# If no fruits are found, then the game moves on to checking for collisions between snakes and fruits.
# If two snakes intersect, then their scores are incremented by 10.
# If a snake collides with a wall or another snake, then that snake dies and game over conditions are triggered.
# Finally, touching any part of a snake causes it to die and also triggers game over conditions.
# The code will check to see if two positions in the snake body are equal.
# If they are, then the score is incremented by 10 and the game_over() function is called.
# If a player touches the snake body at any point, then the game_over() function will be called.