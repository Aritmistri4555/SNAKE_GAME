import pygame
import random
pygame.init()

width = 600
height =700 

#color=========================================
green = (0,255,0)
red = (255,25,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)

# =========================================================
game_display = pygame.display.set_mode((width,height ))
pygame.display.set_caption("snake game")

def text(text, color, x,y, size):
    font= pygame.font.SysFont("arial",size)
    screentext = font.render(text,True,color)
    game_display.blit(screentext,[x,y])
def plotsnake(window, color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window, color,[x,y,snake_size,snake_size])


def game_load():
    snake_X = 100 # X position
    snake_Y =height/2 # Y position
    snake_size =10 # width = 10 and also height = 10
    food_X = random.randint(0,width/2)
    food_Y =random.randint(0,height/2)
    food_size = 10
    snake_x_val = 0
    snake_y_val =0
    score = 0
    fps = 10
    snake_list = []
    snake_length = 1
    game_over = False

    exit_game = False
    clock = pygame.time.Clock()


    while not exit_game:
        if game_over:
            game_display.fill(white)
            text("==========Snake game======================", black,10,200,50 )
            text("Game Over!!! press Q to quit and C to continue ", blue,100,300,25)
            text("===== Developed BY Arit Mistri=====", blue,100,400,25)
            for  event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: 
                        exit_game = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_load()
            clock.tick(fps)
            pygame.display.update()


        else:

            for  event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_LEFT:
                        snake_x_val = -10
                        snake_y_val = 0
                    if event.key == pygame.K_RIGHT:
                        snake_x_val = +10
                        snake_y_val = 0
                    if event.key == pygame.K_UP:
                        snake_x_val = 0
                        snake_y_val = -10
                    if event.key == pygame.K_DOWN:
                        snake_x_val = 0
                        snake_y_val = +10
            if snake_X >= width or snake_X < 0 or  snake_Y >= height or snake_Y < 0 :
                # exit_game = True
                game_over = True        
            
            snake_X = snake_X + snake_x_val
            snake_Y = snake_Y + snake_y_val
            if abs(snake_X-food_X )<=5 and abs(snake_Y-food_Y)<=5:
                score = score+10
                food_X = random.randint(0,width/2)
                food_Y =random.randint(0,height/2)
                snake_length =snake_length+5

            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snake_list.append(head)



            if len(snake_list) > snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True
            
            game_display.fill(black)
            text("Score : " + str(score), yellow,5,5,25)
            # pygame.draw.circle(game_display, red, [food_X, food_Y],food_size)
            pygame.draw.rect(game_display, red, [food_X, food_Y,food_size, food_size])
            plotsnake(game_display,green,snake_list,snake_size)
            # pygame.draw.rect(game_display, green, [snake_X, snake_Y,snake_size,snake_size])

            clock.tick(fps)
            pygame.display.update()
            
        

            


    pygame.quit()
    quit()
       
game_load()