import pygame as pg
from pygame import mixer


# иницилизируем музыку
pg.mixer.pre_init(44100, -16, 2, 2048)
pg.mixer.init()

#инициализируем игру
pg.init()
# загружаем спрайты
PLITVERTICAL = pg.image.load('Sprites/plitavertical.png')
PLITHORIZONTAL = pg.image.load('Sprites/plitahorizontal.png')
LONGPLITHORIZONTAL = pg.image.load('Sprites/longplitahorizontal.png')
LONGPLITVERTICAL = pg.image.load('Sprites/longplitavertical.png')
BGLEVEL = pg.image.load('Sprites/BG.jpg')
BUTTONMENU = pg.image.load('Sprites/Buttonmenu.png')
BUTTONREPLAY = pg.image.load('Sprites/Buttonreplay.png')
BUTTONNEXT = pg.image.load('Sprites/Buttonnext.png')

BUTTONPAUSEMENU = pg.image.load('Sprites/Buttonpausemenu.png')
BUTTONPAUSECONTINUE = pg.image.load('Sprites/Buttonpausecontinie.png')
BUTTONPAUSEREPLAY = pg.image.load('Sprites/Buttonpausereplay.png')
    
TEXTPAUSE = pg.image.load('Sprites/textpause.png')


GUNIMG = pg.image.load('Sprites/gun0.png')
PLATEIMG = pg.image.load('Sprites/plate.png')

BALLIMG = pg.image.load('Sprites/ball.png')

gunImg = pg.image.load('Sprites/gun180.png')

VOLUMEPLAYIMG = pg.image.load('Sprites/volumeplay.png')

PORTALIMG = pg.image.load('Sprites/portal.png')
VOLUMESTOPIMG = pg.image.load('Sprites/volumemute.png')
TEXTCOMPLETE = pg.image.load('Sprites/textlevelcompleted.png')
                    
TEXTFINISH = pg.image.load('Sprites/textfinishgame.png')
TEXTLEVELS = pg.image.load('Sprites/textLVL.png')

BUTTONEXITLVL = pg.image.load('Sprites/Buttonexitlevels.png')
BONUSLVLIMG = pg.image.load('Sprites/bonuslevel.png')

BGLEVELS = pg.image.load('Sprites/BGLEVELS.png')
TEXTGAME = pg.image.load('Sprites/textnameOfTheGame.png')
BGMENU = pg.image.load('Sprites/BGMENU.png')
BUTTONPLAY = pg.image.load('Sprites/Buttonplay.png')
BUTTONEXIT = pg.image.load('Sprites/Buttonexit.png')
   

def level1():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 7
    plitsImg = [PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL]
    plitsX = [300, 600, 900, 750, 950, 1150, 1050]
    plitsY = [370, 100, 380, 480, 700, 500, 400]
    plitsPosition = ['vertical', 'vertical', 'vertical', 'horizontal', 'horizontal', 'vertical', 'horizontal']
    portalX = 1430
    portalY = 50
    level = 1
    game()

def level2():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 7
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL]
    plitsX = [1000, 900, 1000, 700, 500, 1000, 1270]
    plitsY = [500, 450, 400, 100, 300, 800, 500]
    plitsPosition = ['horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'vertical', 'vertical']
    portalX = 1430
    portalY = 700
    level = 2
    game()

def level3():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 7
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITHORIZONTAL]
    plitsX = [900, 500, 650, 750, 850, 970, 800]
    plitsY = [600, 250, 100, 250, 100, 220, 370]
    plitsPosition = ['horizontal', 'vertical', 'vertical', 'vertical', 'horizontal', 'horizontal', 'horizontal']
    portalX = 1300
    portalY = 800
    level = 3
    game()

def level4():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 6
    plitsImg = [PLITHORIZONTAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITHORIZONTAL,]
    plitsX = [850, 400, 200, 400, 880, 1200]
    plitsY = [650, 200, 400, 600, 100, 500]
    plitsPosition = ['horizontal', 'horizontal', 'horizontal', 'vertical', 'vertical', 'horizontal']
    portalX = 1430
    portalY = 250
    level = 4
    game()

def level5():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 6
    plitsImg = [PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL]
    plitsX = [500, 800, 1000, 1270, 1020, 600]
    plitsY = [570, 250, 500, 250, -20, -20]
    plitsPosition = ['vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical']
    portalX = 100
    portalY = 520
    level = 5
    game()

def level6():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 9
    plitsImg = [PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL]
    plitsX = [1430, 1200, 1050, 700, 850, 1000, 700, 900, 650]
    plitsY = [670, 400, 550,    200, 50, 200, 450, 600 ,800]
    plitsPosition = ['vertical', 'horizontal', 'vertical', 'vertical', 'horizontal', 'horizontal', 'horizontal', 'vertical', 'vertical']
    portalX = 100
    portalY = 220
    level = 6
    game()

def level7():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 9
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITHORIZONTAL]
    plitsX = [1100, 1400, 1100, 850, 870, 650, 630, 370, 450]
    plitsY = [600, 350, 100,    350, 780, 500, 100, 350, 700]
    plitsPosition = ['horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'horizontal', 'vertical', 'horizontal', 'horizontal']
    portalX = 100
    portalY = 300
    level = 7
    game()

def level8():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 7
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL]
    plitsX = [1000, 1200, 950, 600, 400, -30, 750]
    plitsY = [500, 350, 100, 500, 250, 670, 750]
    plitsPosition = ['horizontal', 'vertical', 'vertical', 'vertical', 'horizontal', 'vertical', 'vertical']
    portalX = 50
    portalY = 750
    level = 8
    game()

def level9():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 8
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITHORIZONTAL]
    plitsX = [900, 1150, 1050, 900, 770, 350, 500, 650]
    plitsY = [400, 200, 100, 300, 100, 500, 650, 500]
    plitsPosition = ['horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'vertical', 'vertical', 'horizontal']
    portalX = 560
    portalY = 450
    level = 9
    game()

def level10():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 10
    plitsImg = [PLITHORIZONTAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL]
    plitsX = [620, 700, 1200, 1300, 1100, 800, 900, 1300, 1200, 950]
    plitsY = [100, -20, 500, 400, 200, 500, 600, 200, 50, 50]
    plitsPosition = ['horizontal', 'horizontal', 'vertical', 'horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'horizontal', 'vertical']
    portalX = 450
    portalY = 600
    level = 10
    game()

def level11():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 8
    plitsImg = [PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL]
    plitsX = [400, 500, 600, 1300, 200, 475, 1150, 1075]
    plitsY = [120, 25, 125, 550, 475, 750, 50, 800]
    plitsPosition = ['vertical', 'vertical', 'horizontal', 'horizontal', 'vertical', 'vertical', 'vertical', 'vertical']
    portalX = 1350
    portalY = 250
    level = 11
    game()

def level12():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 7
    plitsImg = [PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL]
    plitsX = [520, 1100, 970, 400, 400, 20, 1000]
    plitsY = [150, 700, 800, 220, 10, 400, 300]
    plitsPosition = ['vertical', 'horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'horizontal']
    portalX = 200
    portalY = 600
    level = 12
    game()

def level13():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 8
    plitsImg = [PLITVERTICAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL, ]
    plitsX = [1100, 900, 500, 400, 900, 1050, 1200, 200]
    plitsY = [350, 600, 200, 300, 800, 600, 800, 500]
    plitsPosition = ['vertical', 'horizontal', 'horizontal', 'horizontal', 'horizontal', 'vertical', 'vertical', 'horizontal']
    portalX = 1400
    portalY = 600
    level = 13
    game()

def level14():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 13
    plitsImg = [PLITHORIZONTAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITVERTICAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITVERTICAL]
    plitsX = [500, 700, 380, 250, 100, 250, 500, 620, 900,  1200, 1000, 900666, 1020]
    plitsY = [150, 300, 600, 400, 600, 750, 750, 500, 200, 400, 600, 200, 180]
    plitsPosition = ['horizontal', 'horizontal', 'vertical', 'horizontal', 'vertical', 'horizontal',
                     'horizontal', 'vertical', 'vertical', 'vertical', 'horizontal', 'horizontal', 'vertical']
    portalX = 790
    portalY = 725
    level = 14
    game()

def level15():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 12
    plitsImg = [PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL]
    plitsX = [550, 450, 250, 500, 700, 450, 900, 1000, 1200, 950, 1100, 960]
    plitsY = [150, 0, 250, 500, 300, 250, 200, 50, 300,      500, 600, 710]
    plitsPosition = ['horizontal', 'vertical', 'horizontal', 'vertical', 'horizontal', 'vertical',
                     'horizontal', 'vertical', 'horizontal', 'vertical', 'vertical', 'vertical']
    portalX = 550
    portalY = 300
    level = 15
    game()

def bonus_level():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    global level
    # Плиты
    numOfPlits = 35
    plitsImg = [LONGPLITHORIZONTAL, LONGPLITVERTICAL,
                LONGPLITHORIZONTAL, LONGPLITVERTICAL,
                PLITHORIZONTAL, PLITHORIZONTAL,
                PLITHORIZONTAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL,PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                PLITVERTICAL, PLITVERTICAL,
                ]
    plitsX = [0, 0, 0, 1518, 350, 700, 1100,
              150, 350, 530, 700, 900, 1100, 1300,
              50, 250, 430, 600, 800, 1000, 1200,
              150, 350, 530, 700, 900, 1100, 1300,
              250, 450, 630, 800, 1000, 1200, 1400]
    plitsY = [0, 0, 866, 0, 650, 650, 650, 500, 500, 500, 500, 500, 500, 500,
              350, 350, 350, 350, 350, 350, 350,
              200, 200, 200, 200, 200, 200, 200,
              50, 50, 50, 50, 50, 50, 50]
    plitsPosition = ['longhorizontal', 'longvertical', 'longhorizontal', 'longvertical',
                     'horizontal', 'horizontal', 'horizontal',
                     'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical',
                     'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical',
                     'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical',
                     'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical', 'vertical']
    portalX = 1400
    portalY = 750
    level = 0
    game()


# функция окна игры
def game():
    global numOfPlits
    global plitsX
    global plitsY
    global plitsImg
    global plitsPosition
    global portalX
    global portalY
    #создаем окно
    screen = pg.display.set_mode((1552, 900))

    # пауза
    pauseBg = pg.Surface((1600, 900), pg.SRCALPHA)  # per-pixel alpha
    pauseBg.fill((255, 255, 255, 128))
    pause = False
    pauseButtonMenuX = 400
    pauseButtonMenuY = 600
    pauseButtonContinueX = 1000
    pauseButtonContinueY = 600
    buttonPauseReplayX = 700
    buttonPauseReplayY = 600

    # функция паузы
    def pausa():
        if pause == True:
            screen.blit(pauseBg, (0,0))
            text('Уровень ' + str(level), 100, 540, 350, 230, 230, 100)
            screen.blit(BUTTONPAUSEMENU, (pauseButtonMenuX, pauseButtonMenuY))
            screen.blit(BUTTONPAUSECONTINUE, (pauseButtonContinueX, pauseButtonContinueY))
            screen.blit(BUTTONPAUSEREPLAY, (buttonPauseReplayX, buttonPauseReplayY))
            screen.blit(TEXTPAUSE, (650, 30))

    #музыка
    mixer.music.load('Musics/bgmusic.wav')
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)
    music_play = True

    def play_music(music):
        Sound = mixer.Sound(music)
        Sound.play()
        Sound.set_volume(volume)

    charged = True
    position = 3

    if level < 6:
        #Пушка
        gunImg = pg.image.load('Sprites/gun0.png')
        plateImg = pg.image.load('Sprites/plate.png')
        plateX = 704
        plateY = 760
        gunX = 704
        gunY = 750

        #Снаряд
        ballImg = pg.image.load('Sprites/ball.png')
        ballX = 736
        ballY = 770
        ballMoveX = 0
        ballMoveY = 1

    elif level > 5 and level < 11:
        #Пушка
        gunImg = pg.image.load('Sprites/gun0.png')
        plateImg = pg.image.load('Sprites/plate.png')
        plateX = 1300
        plateY = 760
        gunX = 1300
        gunY = 750

        #Снаряд
        ballImg = pg.image.load('Sprites/ball.png')
        ballX = 1336
        ballY = 770
        ballMoveX = 0
        ballMoveY = 1

    elif level > 10:
        #Пушка
        gunImg = pg.image.load('Sprites/gun180.png')
        plateImg = pg.image.load('Sprites/plate.png')
        plateX = 704
        plateY = -60
        gunX = 704
        gunY = 10

        #Снаряд
        ballImg = pg.image.load('Sprites/ball.png')
        ballX = 736
        ballY = 10
        ballMoveX = 0
        ballMoveY = 1

    # значок звука
    volumeImg = pg.image.load('Sprites/volumeplay.png')
    volumeX = 10
    volumeY = 10
    volume = 0.5


    #прохождения уровня
    levelCompleted = False

    #портал
    portalImg = pg.image.load('Sprites/portal.png')

    #Функция портала
    def portal(x, y):
        screen.blit(portalImg, (x,y))

    #Функция конечных кнопок
    def end_buttons():
        if level < 15:
            screen.blit(BUTTONMENU, (300, 650))
            screen.blit(BUTTONREPLAY, (700, 650))
            screen.blit(BUTTONNEXT, (1100, 650))
        else:
            screen.blit(BUTTONMENU, (600, 650))
            screen.blit(BUTTONREPLAY, (900, 650))

    # функция значка звука
    def music():
        nonlocal volumeImg
        nonlocal music_play
        nonlocal volume
        if music_play == True:
            music_play = False
            mixer.music.stop()
            volumeImg = pg.image.load('Sprites/volumemute.png')
            volume = 0
        else:
            music_play = True
            mixer.music.play()
            volumeImg = pg.image.load('Sprites/volumeplay.png')
            volume = 0.5

    #Функция пушки
    def gun(x, y, x1, y1):
        screen.blit(gunImg, (x, y))
        screen.blit(plateImg, (x1,y1))

    #Функция плит
    def plits(x, y, i):
        screen.blit(plitsImg[i], (x, y))

    def text(text, size, x, y, r, g, b):
        font = pg.font.Font('freesansbold.ttf', size)
        overText = font.render(text,
                          True, (r, g, b))
        screen.blit(overText, (x, y))

    #Функция снаряда
    def ball(x,y):
        screen.blit(ballImg, (x, y))


    #игровой цикл
    running = True
    while running:

        # отрисываем фон
        screen.fill((0,0,0))
        screen.blit(BGLEVEL, (0, 0))


        # проверяем все события
        for event in pg.event.get():
            # проверка закрытия окна
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                if pause == False:
                    # движение пушки
                    if event.key == pg.K_LEFT:
                        if level < 6:
                            position -= 1
                            if position <= 1:
                                gunImg = pg.image.load('Sprites/gun270.png')
                                gunX = 690
                                gunY = 755
                                position = 1
                                if charged == True:
                                    ballX = 720
                                    ballY = 785
                            elif position == 2:
                                gunImg = pg.image.load('Sprites/gun315.png')
                                gunX = 690
                                if charged == True:
                                    ballX = 715
                                    ballY = 780
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun0.png')
                                gunX = 704
                                gunY = 750
                                if charged == True:
                                    ballX = 736
                                    ballY = 770
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun45.png')
                                gunX = 718
                                if charged == True:
                                    ballX = 752
                                    ballY = 785
                        elif level > 5 and level < 11:
                            position -= 1
                            if position <= 1:
                                gunImg = pg.image.load('Sprites/gun270.png')
                                gunX = 1286
                                gunY = 755
                                position = 1
                                if charged == True:
                                    ballX = 1316
                                    ballY = 785
                            elif position == 2:
                                gunImg = pg.image.load('Sprites/gun315.png')
                                gunX = 1286
                                if charged == True:
                                    ballX = 1311
                                    ballY = 780
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun0.png')
                                gunX = 1300
                                gunY = 750
                                if charged == True:
                                    ballX = 1332
                                    ballY = 770
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun45.png')
                                gunX = 1314
                                if charged == True:
                                    ballX = 1348
                                    ballY = 785
                        elif level > 10:
                            position -= 1
                            if position <= 1:
                                gunImg = pg.image.load('Sprites/gun270.png')
                                gunX = 690
                                gunY = 5
                                position = 1
                                if charged == True:
                                    ballX = 720
                                    ballY = 40
                            elif position == 2:
                                gunImg = pg.image.load('Sprites/gun225.png')
                                gunX = 690
                                if charged == True:
                                    ballX = 750
                                    ballY = 10
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun180.png')
                                gunX = 704
                                gunY = 10
                                if charged == True:
                                    ballX = 736
                                    ballY = 10
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun135.png')
                                gunX = 718
                                if charged == True:
                                    ballX = 725
                                    ballY = 10


                    if event.key == pg.K_RIGHT:
                        if level < 6:
                            position += 1
                            if position == 2:
                                gunImg = pg.image.load('Sprites/gun315.png')
                                gunX = 690
                                if charged == True:
                                    ballX = 715
                                    ballY = 785
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun0.png')
                                gunX = 704
                                gunY = 750
                                if charged == True:
                                    ballX = 736
                                    ballY = 770
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun45.png')
                                gunX = 718
                                if charged == True:
                                    ballX = 752
                                    ballY = 780
                            elif position >= 5:
                                gunImg = pg.image.load('Sprites/gun90.png')
                                gunX = 718
                                gunY = 755
                                position = 5
                                if charged == True:
                                    ballX = 752
                                    ballY = 785
                        elif 5 < level < 11:
                            position += 1
                            if position == 2:
                                gunImg = pg.image.load('Sprites/gun315.png')
                                gunX = 1284
                                if charged == True:
                                    ballX = 1311
                                    ballY = 785
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun0.png')
                                gunX = 1300
                                gunY = 750
                                if charged == True:
                                    ballX = 1332
                                    ballY = 770
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun45.png')
                                gunX = 1314
                                if charged == True:
                                    ballX = 1348
                                    ballY = 780
                            elif position >= 5:
                                gunImg = pg.image.load('Sprites/gun90.png')
                                gunX = 1314
                                gunY = 755
                                position = 5
                                if charged == True:
                                    ballX = 1348
                                    ballY = 785
                        elif level > 10:
                            position += 1
                            if position == 2:
                                gunImg = pg.image.load('Sprites/gun225.png')
                                gunX = 690
                                if charged == True:
                                    ballX = 750
                                    ballY = 10
                            elif position == 3:
                                gunImg = pg.image.load('Sprites/gun180.png')
                                gunX = 704
                                gunY = 10
                                if charged == True:
                                    ballX = 736
                                    ballY = 10
                            elif position == 4:
                                gunImg = pg.image.load('Sprites/gun135.png')
                                gunX = 718
                                if charged == True:
                                    ballX = 725
                                    ballY = 10
                            elif position >= 5:
                                gunImg = pg.image.load('Sprites/gun90.png')
                                gunX = 718
                                gunY = 5
                                position = 5
                                if charged == True:
                                    ballX = 760
                                    ballY = 40

                    if event.key == pg.K_SPACE:
                        if charged:
                            if level < 11:
                                if position == 1:
                                    ballMoveY = 0
                                    ballMoveX = 1
                                elif position == 2:
                                    ballMoveX = 1
                                    ballMoveY = 1
                                elif position == 3:
                                    ballMoveY = 1
                                    ballMoveX = 0
                                elif position == 4:
                                    ballMoveY = 1
                                    ballMoveX = -1
                                elif position == 5:
                                    ballMoveY = 0
                                    ballMoveX = -1
                            elif level > 10:
                                if position == 1:
                                    ballMoveY = 0
                                    ballMoveX = 1
                                elif position == 2:
                                    ballMoveX = 1
                                    ballMoveY = -1
                                elif position == 3:
                                    ballMoveY = -1
                                    ballMoveX = 0
                                elif position == 4:
                                    ballMoveY = -1
                                    ballMoveX = -1
                                elif position == 5:
                                    ballMoveY = 0
                                    ballMoveX = -1
                                charged = False
                            charged = False
                            if levelCompleted == False:
                                play_music('Musics/fire.wav')

                    if event.key == pg.K_r:
                        if levelCompleted == False:
                            if level < 6:
                                if position <= 1:
                                    ballX = 720
                                    ballY = 785
                                elif position == 2:
                                    ballX = 715
                                    ballY = 785
                                elif position == 3:
                                    ballX = 736
                                    ballY = 770
                                elif position == 4:
                                    ballX = 752
                                    ballY = 780
                                elif position >= 5:
                                    ballX = 752
                                    ballY = 785
                            elif 5 < level < 11:
                                if position <= 1:
                                    ballX = 1316
                                    ballY = 785
                                elif position == 2:
                                    ballX = 1311
                                    ballY = 785
                                elif position == 3:
                                    ballX = 1332
                                    ballY = 770
                                elif position == 4:
                                    ballX = 1348
                                    ballY = 780
                                elif position >= 5:
                                    ballX = 1348
                                    ballY = 785
                            elif level > 10:
                                if position <= 1:
                                    ballX = 720
                                    ballY = 40
                                elif position == 2:
                                    ballX = 750
                                    ballY = 10
                                elif position == 3:
                                    ballX = 736
                                    ballY = 10
                                elif position == 4:
                                    ballX = 725
                                    ballY = 10
                                elif position >= 5:
                                    ballX = 760
                                    ballY = 40
                            ballMoveX = 0
                            ballMoveY = 0
                            charged = True
                            play_music('Musics/reload.wav')

                if event.key == pg.K_ESCAPE:
                    if pause == False:
                        pause = True
                    else:
                        pause = False


            # реализовываем поворот плит при нажатии
            if event.type == pg.MOUSEBUTTONDOWN:
                coords = event.pos
                # плиты и мячик
                if charged:
                    for i in range(numOfPlits):
                        if plitsX[i] < coords[0] < plitsX[i] + 96 and plitsY[i] < coords[1] < plitsY[i] + 96:
                            if plitsPosition[i] == 'vertical':
                                plitsPosition[i] = 'horizontal'
                                plitsImg[i] = PLITHORIZONTAL
                            elif plitsPosition[i] == 'horizontal':
                                plitsPosition[i] = 'vertical'
                                plitsImg[i] = PLITVERTICAL
                            play_music('Musics/povorot.wav')
                # значок мызыки
                if volumeX < coords[0] < volumeX + 32 and volumeY < coords[1] < volumeY + 32:
                    music()
                if level < 15:
                    # кнопка в меню
                    if levelCompleted == True:
                        if 300 < coords[0] < 300 + 140 and 650 < coords[1] < 650 + 103:
                            running = False
                            mixer.music.stop()
                            play_music('Musics/buttonclick.wav')
                            mainmenurun()
                    # кнопка заново
                    if levelCompleted == True:
                        if 700 < coords[0] < 700 + 140 and 650 < coords[1] < 650 + 103:
                            play_music('Musics/buttonclick.wav')
                            if level == 0:
                                bonus_level()
                            elif level == 1:
                                level1()
                            elif level == 2:
                                level2()
                            elif level == 3:
                                level3()
                            elif level == 3:
                                level3()
                            elif level == 4:
                                level4()
                            elif level == 5:
                                level5()
                            elif level == 6:
                                level6()
                            elif level == 7:
                                level7()
                            elif level == 8:
                                level8()
                            elif level == 9:
                                level9()
                            elif level == 10:
                                level10()
                            elif level == 11:
                                level11()
                            elif level == 12:
                                level12()
                            elif level == 13:
                                level13()
                            elif level == 14:
                                level14()
                            elif level == 15:
                                level15()

                            running = False
                            mixer.music.stop()
                    # кнопка дальше
                    if levelCompleted == True:
                        if 1100 < coords[0] < 1100 + 140 and 650 < coords[1] < 650 + 103:
                            mixer.music.stop()
                            play_music('Musics/buttonclick.wav')
                            if level == 1:
                                level2()
                            elif level == 2:
                                level3()
                            elif level == 3:
                                level4()
                            elif level == 4:
                                level5()
                            elif level == 5:
                                level6()
                            elif level == 6:
                                level7()
                            elif level == 7:
                                level8()
                            elif level == 8:
                                level9()
                            elif level == 9:
                                level10()
                            elif level == 10:
                                level11()
                            elif level == 11:
                                level12()
                            elif level == 12:
                                level13()
                            elif level == 13:
                                level14()
                            elif level == 14:
                                level15()
                            running = False
                            mixer.music.stop()
                else:
                    if levelCompleted == True:
                        if 600 < coords[0] < 600 + 140 and 650 < coords[1] < 650 + 103:
                            running = False
                            mixer.music.stop()
                            play_music('Musics/buttonclick.wav')
                            mainmenurun()
                    # кнопка заново
                    if levelCompleted == True:
                        if 900 < coords[0] < 900 + 140 and 650 < coords[1] < 650 + 103:
                            play_music('Musics/buttonclick.wav')
                            if level == 0:
                                bonus_level()
                            elif level == 1:
                                level1()
                            elif level == 2:
                                level2()
                            elif level == 3:
                                level3()
                            elif level == 3:
                                level3()
                            elif level == 4:
                                level4()
                            elif level == 5:
                                level5()
                            elif level == 6:
                                level6()
                            elif level == 7:
                                level7()
                            elif level == 8:
                                level8()
                            elif level == 9:
                                level9()
                            elif level == 10:
                                level10()
                            elif level == 11:
                                level11()
                            elif level == 12:
                                level12()
                            elif level == 13:
                                level13()
                            elif level == 14:
                                level14()
                            elif level == 15:
                                level15()

                            running = False
                            mixer.music.stop()

                # кнопка в меню из паузы
                if pause == True:
                    if pauseButtonMenuX < coords[0] < pauseButtonMenuX + 202 and pauseButtonMenuY < coords[1] < pauseButtonMenuY + 176:
                        running = False
                        mixer.music.stop()
                        play_music('Musics/buttonclick.wav')
                        menulevelsrun()
                # кнопка продолжить из пауза
                    if pauseButtonContinueX < coords[0] < pauseButtonContinueX + 202 and pauseButtonContinueY < coords[1] < pauseButtonContinueY + 176:
                        play_music('Musics/buttonclick.wav')
                        pause = False
                # кнопка заново из паузы
                    if buttonPauseReplayX < coords[0] < buttonPauseReplayX + 140 and buttonPauseReplayY  < coords[1] < buttonPauseReplayY + 103:
                        play_music('Musics/buttonclick.wav')
                        if level == 0:
                            bonus_level()
                        elif level == 1:
                            level1()
                        elif level == 2:
                            level2()
                        elif level == 3:
                            level3()
                        elif level == 3:
                            level3()
                        elif level == 4:
                            level4()
                        elif level == 5:
                            level5()
                        elif level == 6:
                            level6()
                        elif level == 7:
                            level7()
                        elif level == 8:
                            level8()
                        elif level == 9:
                            level9()
                        elif level == 10:
                            level10()
                        elif level == 11:
                            level11()
                        elif level == 12:
                            level12()
                        elif level == 13:
                            level13()
                        elif level == 14:
                            level14()
                        elif level == 15:
                            level15()
                        running = False

        # функция паузы
        pausa()

        if pause == False:

            # проверка вылета пули
            if ballY < 0 or ballX < 0 or ballX > 1568 or ballY > 868:
                if levelCompleted == False:
                    play_music('Musics/reload.wav')
                charged = True
                if levelCompleted == False:
                    if level < 6:
                        if position <= 1:
                            ballX = 720
                            ballY = 785
                        elif position == 2:
                            ballX = 715
                            ballY = 785
                        elif position == 3:
                            ballX = 736
                            ballY = 770
                        elif position == 4:
                            ballX = 752
                            ballY = 780
                        elif position >= 5:
                            ballX = 752
                            ballY = 785
                    elif 5 < level < 11:
                        if position <= 1:
                            ballX = 1316
                            ballY = 785
                        elif position == 2:
                            ballX = 1311
                            ballY = 785
                        elif position == 3:
                            ballX = 1332
                            ballY = 770
                        elif position == 4:
                            ballX = 1348
                            ballY = 780
                        elif position >= 5:
                            ballX = 1348
                            ballY = 785
                    elif level > 10:
                        if position <= 1:
                            ballX = 720
                            ballY = 40
                        elif position == 2:
                            ballX = 750
                            ballY = 10
                        elif position == 3:
                            ballX = 736
                            ballY = 10
                        elif position == 4:
                            ballX = 725
                            ballY = 10
                        elif position >= 5:
                            ballX = 760
                            ballY = 40

            # проверка попадания шарика в портал
            if ballX > portalX and ballX + 32 < portalX + 96 and ballY > portalY and ballY + 32 < portalY + 96:
                for i in range(numOfPlits):
                    plitsX[i] = 2000
                ballX = 2030
                ballY = 2030
                portalX = 2000
                portalY = 2000
                ballMoveX = 0
                ballMoveY = 0
                gunX = 2000
                plateX = 2000
                if levelCompleted == False:
                    mixer.music.stop()
                    mixer.music.load('Musics/win.wav')
                    mixer.music.play()
                    mixer.music.set_volume(0.6)
                    if level < 15:
                        textwin = pg.image.load('Sprites/textlevelcompleted.png')
                    else:
                        textwin = pg.image.load('Sprites/textfinishgame.png')
                levelCompleted = True
                text('Уровень ' + str(level), 100, 540, 350, 230, 230, 100)
                screen.blit(textwin, (300, 0))
                # рисуем конечные кнопки
                end_buttons()


            # проверка столкновения плит и шарика
            if charged == False:
                for i in range(numOfPlits):
                    if plitsPosition[i] == 'vertical':
                        if (plitsY[i] - 15 < ballY + 32 and ballY < plitsY[i] + 111) and (plitsX[i] + 32 < ballX + 32 and ballX < plitsX[i] + 64):
                            if plitsY[i] < ballY + 32 and ballY < plitsY[i] + 96:
                                if ballMoveX == 1:
                                    ballMoveX = -1
                                elif ballMoveX == -1:
                                    ballMoveX = 1
                            elif ballY + 32 < plitsY[i] or ballY > plitsY[i] + 96:
                                if ballMoveY == 1:
                                    ballMoveY = -1
                                elif ballMoveY == -1:
                                    ballMoveY = 1
                            play_music('Musics/rebound.wav')

                    elif plitsPosition[i] == 'horizontal':
                        if (plitsY[i] + 32 < ballY + 32 and ballY < plitsY[i] + 64) and (plitsX[i] < ballX + 32 and ballX < plitsX[i] + 110):
                            if plitsX[i] < ballX + 32 and ballX < plitsX[i] + 96:
                                if ballMoveY == 1:
                                    ballMoveY = -1
                                elif ballMoveY == -1:
                                    ballMoveY = 1
                            elif ballX + 32 < plitsX[i] or ballX > plitsX[i] + 96:
                                if ballMoveX == 1:
                                    ballMoveX = -1
                                elif ballMoveX == -1:
                                    ballMoveX = 1
                            play_music('Musics/rebound.wav')

                    elif plitsPosition[i] == 'longhorizontal':
                        if plitsY[i] < ballY + 32 and ballY < plitsY[i] + 30:
                            if ballMoveY == 1:
                                ballMoveY = -1
                            elif ballMoveY == -1:
                                ballMoveY = 1
                            play_music('Musics/rebound.wav')

                    elif plitsPosition[i] == 'longvertical':
                        if plitsX[i] < ballX + 32 and ballX < plitsX[i] + 30:
                            if ballMoveX == 1:
                                ballMoveX = -1
                            elif ballMoveX == -1:
                                ballMoveX = 1
                            play_music('Musics/rebound.wav')

            #полёт пули и её отрисовка
            if charged == False:
                for i in range(0,15):
                    ballX -= ballMoveX
                    ballY -= ballMoveY
                    ball(ballX, ballY)

            # отрисовываем плиты
            for i in range(numOfPlits):
                plits(plitsX[i], plitsY[i], i)

            # отрисовываем пушку
            gun(gunX, gunY, plateX, plateY)
            portal(portalX, portalY)

        screen.blit(volumeImg, (volumeX, volumeY))
        # обновляем экран
        pg.display.update()

# функция меню уровней
def menulevelsrun():
    #создаем окно
    screen1 = pg.display.set_mode((1280, 850))

    # текст выбор уровня
    textlevels = pg.image.load('Sprites/textLVL.png')

    # текст
    def text(text, size, x, y, r,g,b):
        font = pg.font.Font('freesansbold.ttf', size)
        overText = font.render(text,
                          True, (r, g, b))
        screen1.blit(overText, (x, y))

    # кнопка выйти
    buttonexitImg = pg.image.load('Sprites/Buttonexitlevels.png')
    buttonexitX = 575
    buttonexitY = 700

    # расположения текста
    levelsX = []
    levelsY = []
    levelImg = []
    colortext = [40, 40, 255]
    for i in range(0,15):
        levelImg.append(pg.image.load('Sprites/level.png'))
    onelevelX = 140
    onelevelY = 150
    for i in range(0, 15):
        if i == 5:
            onelevelX = 140
            onelevelY += 150
        elif i == 10:
            onelevelX = 140
            onelevelY += 150
        levelsX.append(onelevelX)
        levelsY.append(onelevelY)
        onelevelX += 220

    # бонус уровень
    bonuslevelImg = pg.image.load('Sprites/bonuslevel.png')


    #Фон
    background = pg.image.load('Sprites/BGLEVELS.png')

    #игровой цикл
    running1 = True
    while running1:

        # отрисываем фон
        screen1.fill((0, 0, 0))
        screen1.blit(background, (0, 0))

        # проверяем все события
        for event in pg.event.get():
            # проверка закрытия окна
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in range(0, 15):
                    if levelsX[i] < pos[0] < levelsX[i] + 120 and levelsY[i] < pos[1] < levelsY[i] + 120:
                        Sound = mixer.Sound('Musics/buttonclick.wav')
                        Sound.play()
                        levelImg[i] = pg.image.load('Sprites/levelclick.png')
                        colortext = [168, 183, 233]
                        if i == 0:
                            level1()
                        elif i == 1:
                            level2()
                        elif i == 2:
                            level3()
                        elif i == 3:
                            level4()
                        elif i == 4:
                            level5()
                        elif i == 5:
                            level6()
                        elif i == 6:
                            level7()
                        elif i == 7:
                            level8()
                        elif i == 8:
                            level9()
                        elif i == 9:
                            level10()
                        elif i == 10:
                            level11()
                        elif i == 11:
                            level12()
                        elif i == 12:
                            level13()
                        elif i == 13:
                            level14()
                        elif i == 14:
                            level15()

                if 575 < pos[0] < 575 + 128 and 730 + 40 < pos[1] < 730 + 80:
                    Sound = mixer.Sound('Musics/buttonclick.wav')
                    Sound.play()
                    mainmenurun()

                if 580 < pos[1] < 580 + 120 and 608 < pos[1] < 608 + 120:
                    Sound = mixer.Sound('Musics/buttonclick.wav')
                    Sound.play()
                    bonus_level()


        for i in range(0, 15):
            if i < 5:
                screen1.blit(levelImg[i], (levelsX[i], levelsY[i]))
            elif 4 < i < 10:
                screen1.blit(pg.image.load('Sprites/level2.png'), (levelsX[i], levelsY[i]))
            elif i > 9:
                screen1.blit(pg.image.load('Sprites/level3.png'), (levelsX[i], levelsY[i]))
            if i > 8:
                text(str(i + 1), 64, levelsX[i] + 23, levelsY[i] + 30, colortext[0], colortext[1], colortext[2])
            else:
                text(str(i + 1), 64, levelsX[i] + 42, levelsY[i] + 30, colortext[0], colortext[1], colortext[2])

        # текст "Выбор уровней"
        screen1.blit(textlevels, (350, -70))

        # кнопка бонусный уровень
        screen1.blit(bonuslevelImg, (580,608))

        # отрисовываем кнопку "Выйти"
        screen1.blit(buttonexitImg, (575, 730))
        text(str("бонус"), 32, 595, 655, colortext[0], colortext[1], colortext[2])

        # обновляем экран
        pg.display.update()

# функция главного меню
def mainmenurun():
    #создаем окно
    screen2 = pg.display.set_mode((935, 673))

    #текст
    textgame = pg.image.load('Sprites/textnameOfTheGame.png')

    #Фон
    background = pg.image.load('Sprites/BGMENU.png')

    #Кнопка играть
    buttonplay = pg.image.load('Sprites/Buttonplay.png')
    buttonX = 350
    buttonY = 200

    def buttonplayfunction(x,y):
        screen2.blit(buttonplay, (x, y))

    #Кнопка выйти
    buttonexit = pg.image.load('Sprites/Buttonexit.png')
    button1X = 350
    button1Y = 350

    def buttonexitfunction(x,y):
        screen2.blit(buttonexit, (x, y))

    #игровой цикл
    running2 = True
    while running2:

        # отрисываем фон
        screen2.fill((0, 0, 0))
        screen2.blit(background, (0, 0))

        for event in pg.event.get():
            # проверка закрытия окна
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                coords = event.pos
                if buttonX < coords[0] < buttonX + 256 and buttonY + 64 < coords[1] < buttonY + 192:
                    running2 = False
                    Sound = mixer.Sound('Musics/buttonclick.wav')
                    Sound.play()
                    menulevelsrun()

                if button1X < coords[0] < button1X + 256 and button1Y + 64 < coords[1] < button1Y + 192:
                    Sound = mixer.Sound('Musics/buttonclick.wav')
                    Sound.play()
                    exit()


        # рисуем кнопку играть
        buttonplayfunction(buttonX, buttonY)

        #рисуем кнопку выйти
        buttonexitfunction(button1X, button1Y)

        # рисуем надпись "Rebound Walls"
        screen2.blit(textgame, (150, 10))

        # обновляем экран
        pg.display.update()

mainmenurun()
