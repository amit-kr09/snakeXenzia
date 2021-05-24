import pygame
import random
import os
pygame.init()
pygame.mixer.init()



# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 51, 51)
green = (96, 128, 56)


scr_width = 400
scr_height = 300

# Creating Window
gameWindow = pygame.display.set_mode((scr_width, scr_height))

# Background Image
bgimg = pygame.image.load("image/wel.jpg")
bgimg = pygame.transform.scale(bgimg, (400, 300)).convert_alpha()
bkimg = pygame.image.load("image/back.jpg")
bkimg = pygame.transform.scale(bkimg, (400, 300)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Xenzia")
pygame.display.set_icon(pygame.image.load("image/icon.png"))
pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
def text_scr(text, color, x, y):
    score_txt = font.render(text, True, color)
    gameWindow.blit(score_txt, [x , y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        
        gameWindow.fill(black)
        gameWindow.blit(bgimg, (0, 0))
        text_scr("SNAKE XENZIA", black, 30, 215)
        text_scr("Press SPACEBAR to start game...", (10, 35, 150), 30, 240)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameloop()
            
            pygame.display.update()
            clock.tick(15)

pygame.display.update()

# Creating game loop
def gameloop():
    # Game Specific Variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 15
    food_x = random.randint(80, 320)
    food_y = random.randint(80, 220)
    score = 0
    velocity_x = 0
    velocity_y = 0
    vel = 12
    fps = 15
    snk_list = []
    snk_length = 1
    
    #Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(red)
            text_scr("Game Over! Press Enter to continue...", black, 24, scr_height/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('music/music.mp3')
                        pygame.mixer.music.play()
                        welcome()
                        


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        velocity_x = vel
                        velocity_y = 0
                    if event.key == pygame.K_a:
                        velocity_x = -vel
                        velocity_y = 0
                    if event.key == pygame.K_s:
                        velocity_y = vel
                        velocity_x = 0
                    if event.key == pygame.K_w:
                        velocity_y = -vel
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
            snake_x += velocity_x
            snake_y += velocity_y

            
            gameWindow.fill(green)
            gameWindow.blit(bkimg, (0, 0))

            if abs(snake_x - food_x) < 14 and abs(snake_y - food_y) <14:
                pygame.mixer.music.load('music/bite.mp3')
                pygame.mixer.music.play()
                score +=10
                food_x = random.randint(20, 380)
                food_y = random.randint(20, 280)
                snk_length+=3
                if score > int(hiscore):
                    hiscore = score


            text_scr(f"SCORE : {score}   HIGH SCORE : {hiscore} ", white, 10, 275)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list) > (snk_length):
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > scr_width or snake_y < 0 or snake_y > scr_height:
                game_over = True
                pygame.mixer.music.load('music/gameover.mp3')
                pygame.mixer.music.play()
    
            
            plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()

welcome()
# gameloop()
