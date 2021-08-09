# IMPORTING NECESSARY MODULES
import pygame
import random
import math

# INITIATING PYGAME
pygame.init()

# TITLE AND LOGO
pygame.display.set_caption("DeathRace")
pygame.display.set_icon(pygame.image.load("Photos/motorbike.png"))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# COLOURS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (119, 118, 110)
blue = (0, 0, 255)
magenta = (104, 19, 106)
orange = (226, 88, 34)
lightblue = (40, 108, 130)

# IMAGES
bg = pygame.image.load("Photos/bg2.png")
background = pygame.image.load("Photos/background1.jpg")
bike1 = pygame.image.load("Photos/motorbike.png")
bike1 = pygame.transform.scale(bike1, (100, 100))
my_bike = pygame.image.load("Photos/MainPlay.png")
enemy_bike = pygame.image.load('Photos/enemy.png')
enemy_bike2 = pygame.image.load("Photos/enemy2.png")
enemy_bike2 = pygame.transform.scale(enemy_bike2, (39, 78))
power = pygame.image.load("Photos/power.png")
boul = pygame.image.load("Photos/Boulder.png")
boul = pygame.transform.scale(boul, (100, 100))
bar = pygame.image.load("Photos/Barricade.png")
title = pygame.image.load("Photos/title.png")
bul = pygame.image.load("Photos/Bullet.png")
heartbl = pygame.image.load("Photos/heart.png")
rules = pygame.image.load("Photos/rules.png")
control = pygame.image.load("Photos/controls.png")

# FONTS
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

# BULLET
Bullet = pygame.image.load("Photos/Bullet.png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 20
bullet_state = "ready"

# score
sco = 0


# MUSIC
def crash():
    explosionSound = pygame.mixer.Sound("Music/crash.wav")
    explosionSound.play()


def music():
    pygame.mixer.music.load("Music/background.wav")
    pygame.mixer.music.play(-1)


def motor():
    pygame.mixer.music.load("Music/moto.wav")
    pygame.mixer.music.play(-1)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (190, 250))


def lives(x, y):
    score = font.render("LIVES: ", True, (255, 255, 255))
    screen.blit(score, (x, y))


def score(x, y, ss, colour):
    score = font.render("SCORE: " + str(ss), True, colour)
    screen.blit(score, (x, y))


def enemy(f, g, l):
    screen.blit(l, (f, g))


def Message(size, mess, x_pos, y_pos, colour):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, colour)
    screen.blit(render, (x_pos, y_pos))


def heart(x, y):
    screen.blit(heartbl, (x, y))


def player(x, y):
    screen.blit(my_bike, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(Bullet, (x + 16, y + 10))


def isCollision(varA, varB, varC, varD, disx, disy):
    distancex = math.sqrt(math.pow(varA - varC, 2))
    distancey = math.sqrt(math.pow(varB - varD, 2))
    if distancex < disx and distancey < disy:
        return True
    else:
        return False


def isCollision2(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def start():
    global bullet_y
    global bullet_x
    global bullet_y_change
    global bullet_state
    global sco
    pygame.mixer.music.stop()
    motor()
    count = 3

    f1 = random.randrange(90, 480, 30)
    g1 = -200
    g_change1 = 25

    f2 = random.randrange(90, 480, 30)
    g2 = -200
    g_change2 = 20

    f3 = random.randrange(90, 480, 100)
    g3 = -1000
    g_change3 = 10

    f4 = random.randrange(90, 480, 100)
    g4 = -600
    g_change4 = 10

    f5 = random.randrange(90, 480, 100)
    g5 = -3000
    g_change5 = 10

    if f1 == f2 or f1 == f3 or f1 == f4 or f2 == f3 or f2 == f4 or f3 == f4:
        f1 = random.randrange(90, 480, 30)
        f2 = random.randrange(90, 480, 50)
        f3 = random.randrange(90, 480, 100)
        f4 = random.randrange(90, 480, 100)
    x = 365
    y = 480
    x_change = 0
    y_change = 0
    k = 0
    le_1 = 600
    Rule3 = True
    while Rule3:
        sco = sco + 1
        screen.blit(bg, (0, k))
        screen.blit(bg, (0, k - le_1))
        if k == le_1:
            screen.blit(bg, (k - le_1, 0))
            k = 0
        k = k + 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rule3 = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                    # Rule3 = False
                if event.key == pygame.K_LEFT:
                    x_change = -15

                if event.key == pygame.K_RIGHT:
                    x_change = 15
                if event.key == pygame.K_UP:
                    y_change = -15
                if event.key == pygame.K_DOWN:
                    y_change = 15

                if event.key == pygame.K_SPACE:

                    if bullet_state == 'ready':
                        bullet_x = x
                        bullet_y = y
                        fire_bullet(bullet_x, bullet_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        g1 += g_change1
        g2 += g_change2
        g3 += g_change3
        g4 += g_change4
        g5 += g_change5
        x += x_change
        y += y_change
        if x <= 90:
            x = 90
        if x >= 640:
            x = 640
        if y >= 500:
            y = 500
        if y <= 0:
            y = 0
        # bullet movement
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change
        # bullet collision
        collision1 = isCollision2(f1, g1, bullet_x, bullet_y)
        collision2 = isCollision2(f2, g2, bullet_x, bullet_y)

        if collision1:
            bullet_y = 480
            bullet_state = 'ready'

            f1 = random.randrange(90, 480, 30)
            g1 = -200

        if collision2:
            bullet_y = 480
            bullet_state = 'ready'

            f2 = random.randrange(90, 480, 30)
            g2 = -200
            g_change2 = 20

        if g1 == 600:
            g1 = -200
            f1 = random.randrange(90, 480, 17)
        if g2 == 600:
            g2 = -200
            f2 = random.randrange(90, 480, 17)
        if g3 == 600:
            g3 = -1000
            f3 = random.randrange(90, 480, 100)
        if g4 == 600:
            g4 = -600
            f4 = random.randrange(90, 480, 100)
        if g5 == 600:
            g5 = -200
            f5 = random.randrange(90, 480, 100)

        if isCollision(x, y, f1, g1, 39, 50):
            count = count - 1
            f1 = random.randrange(90, 480, 30)
            g1 = -200
            crash()
        if isCollision(x, y, f2, g2, 39, 50):
            count = count - 1
            f2 = random.randrange(90, 480, 30)
            g2 = -200
            crash()
        if isCollision(x, y, f3, g3, 70, 95):
            count = count - 1
            f3 = random.randrange(90, 480, 100)
            g3 = -1000
            crash()
        if isCollision(x, y, f4, g4, 70, 95):
            count = count - 1
            f4 = random.randrange(90, 480, 100)
            g4 = -600
            crash()
        if isCollision(x, y, f5, g5, 23, 54):
            if count <= 2:
                count = count + 1
                f5 = random.randrange(90, 480, 100)
                g5 = -1500
                explosionSound = pygame.mixer.Sound("Music/Pow.wav")
                explosionSound.play()
            else:
                f5 = random.randrange(90, 480, 100)
                g5 = -1500
        clock.tick(15)
        if count >= 3:
            heart(110, 15)
            heart(145, 15)
            heart(180, 15)
        if count == 2:
            heart(110, 15)
            heart(145, 15)
        if count == 1:
            heart(110, 15)
        if count <= 0:
            gameover()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    Rule3 = False
                    game_intro()
        player(x, y)
        lives(10, 10)
        score(550, 10, sco, white)
        enemy(f1, g1, enemy_bike)
        enemy(f2, g2, enemy_bike2)
        enemy(f3, g3, boul)
        enemy(f4, g4, bar)
        enemy(f5, g5, power)

        pygame.display.update()


def button(x_button, y_button, x, y, x_pad, y_pad, mess_b, colour, colour_hover):
    pygame.draw.rect(screen, colour, [x_button, y_button, x, y])
    Message(53, mess_b, x_button + x_pad, y_button + y_pad, white)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button + x and y_button < mouse[1] < y_button + y:
        pygame.draw.rect(screen, colour_hover, [x_button, y_button, x, y])
        Message(53, mess_b, x_button + x_pad, y_button + y_pad, white)

        if click == (1, 0, 0) and mess_b == "RULES":
            game_rules()
        if click == (1, 0, 0) and mess_b == "QUIT":
            pygame.quit()
            quit()
        if click == (1, 0, 0) and mess_b == "PLAY":
            start()
        if click == (1, 0, 0) and mess_b == "CONTROLS":
            gamecontrols()
        # if click == (1, 0, 0) and mess_b == 'RESUME':
        #   unpaused()


def game_intro():
    music()
    intro = False
    i = 0
    width = 800
    while intro == False:
        screen.fill(black)
        screen.blit(background, (i, 0))
        screen.blit(background, (width + i, 0))

        if i == -width:
            screen.blit(background, (width + i, 0))
            i = 0

        i = i - 8
        screen.blit(bike1, (450, 450))
        screen.blit(bike1, (370, 475))
        screen.blit(title, (50, 40))

        button(55, 290, 219, 40, 63, 5, "PLAY", blue, lightblue)
        button(55, 360, 219, 40, 46, 5, "RULES", blue, lightblue)
        button(55, 430, 219, 40, 2, 5, "CONTROLS", blue, lightblue)
        button(55, 500, 219, 40, 63, 5, "QUIT", magenta, red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
                pygame.quit()
                quit()

        pygame.display.update()


def game_rules():
    j = 0
    width = 800
    rule = True
    while rule:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        screen.blit(rules, (3, 75))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rule = False
                    # game_intro()
            if event.type == pygame.QUIT:
                rule = False
                pygame.quit()
                quit()


def gamecontrols():
    j = 0
    width = 800
    controls = True
    while controls:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        screen.blit(control, (12, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controls = False
                    # game_intro()
            if event.type == pygame.QUIT:
                controls = False
                pygame.quit()
                quit()


def pause():
    global sco
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_r:
                    sco = 0
                    start()
                elif event.key == pygame.K_m:
                    sco = 0
                    game_intro()
        screen.fill(white)
        Message(100, 'Paused', 250, 100, black)
        Message(45, "Press 'c' to continue", 50, 300, blue)
        Message(45, "Press 'r' to restart the game", 50, 350, blue)
        Message(45, "Press 'm' to go to main menu", 50, 400, blue)
        pygame.display.update()
        clock.tick(5)


def gameover():
    global sco
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    sco = 0
                    start()

                elif event.key == pygame.K_m:
                    sco = 0
                    game_intro()
        screen.fill(white)
        Message(100, 'GAME OVER', 200, 100, black)
        score(300, 200, sco, black)

        Message(45, "Press 'r' to restart the game", 50, 350, blue)
        Message(45, "Press 'm' to go to main menu", 50, 400, blue)
        pygame.display.update()
        clock.tick(5)


game_intro()
pygame.display.update()

pygame.quit()
quit()
