import pygame
import sys
import random
    
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
ball_r = 30

#settings for screen
screen = pygame.display.set_mode((1280, 960))

#counter
temp_counter = 0
temp_counter1 = 0
font = pygame.font.Font('freesansbold.ttf', 250)
text = font.render(str(temp_counter), True, (100, 100, 100))
text1 = font.render(str(temp_counter1), True, (100, 100, 100))

textRect = text.get_rect()
textRect.center = (screen_width / 2 - 300, screen_height / 2)
textRect1 = text1.get_rect()
textRect1.center = (screen_width / 2 + 300, screen_height / 2)



#setting for ball
ball_speed_x = 10
ball_speed_y = 10


#settings for players
default_speed = 15
player_speed = 0
opponent_speed = 0

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, ball_r, ball_r)
player = pygame.Rect(screen_width - 30, screen_height / 2 - 100, 5, 200)
opponent = pygame.Rect(20, screen_height / 2 - 100, 5, 200)


#settings of color
background_color = pygame.Color('grey12')
temp_color = pygame.Color('red')
light_grey = (200, 200, 200)

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_animation():
    global ball_speed_x, ball_speed_y, temp_counter, temp_counter1, screen
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.x + ball_r > screen_width or ball.x < 0:
        if ball.x + ball_r > screen_width:
            temp_counter += 1
        else:
            temp_counter1 += 1
            ball.x = screen_width / 2 - 15

        ball.center = (screen_width / 2 - 15, screen_height / 2 - 15)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

        if temp_counter > 9 or temp_counter1 > 9:
            temp_counter = 0
            temp_counter1 = 0

    if ball.y + ball_r > screen_height or ball.y < 0:
        ball_speed_y *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= default_speed
            if event.key == pygame.K_DOWN:
                player_speed += default_speed
            if event.key == pygame.K_w:
                opponent_speed -= default_speed
            if event.key == pygame.K_s:
                opponent_speed += default_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += default_speed
            if event.key == pygame.K_DOWN:
                player_speed -= default_speed
            if event.key == pygame.K_w:
                opponent_speed += default_speed
            if event.key == pygame.K_s:
                opponent_speed -= default_speed
    ball_animation()
    player_animation()
    opponent_animation()
    screen.fill(background_color)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    text = font.render(str(temp_counter), True, (100, 100, 100))
    text1 = font.render(str(temp_counter1), True, (100, 100, 100))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (640, 0), (640, 960))
    pygame.display.flip()
    clock.tick(60)
        
