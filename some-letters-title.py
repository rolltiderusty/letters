#This code was written or inspired by:
#https://blog.penjee.com/mouse-clicked-on-image-in-pygame/

#&

# Joshua Willman wrote the code in here or was the inspiration for it.#
# You can see his work at:#
# https://redhulimachinelearning.com/game-development/draw-images-in-pygame-space-shooter/#


# You will need to install pygame before you can import it, there are plenty of how-to's online.#
import mysql.connector
import pygame, sys
from pygame import *
from time import sleep
# This installs the modules you have imported above (the star means to import all of them, at the moment there is only one).
pygame.init()

#This creates two variables we use to locate our letters.
screenSize_x = 1024
screenSize_y = 600

#Sets a Variable equal to the output of a function containing the location for printing the letters.
DISPLAYSURF = pygame.display.set_mode((screenSize_x, screenSize_y))

# Select the color of the window using RGB numbers#
BLACK = (0,0,0)


#backDrop = pygame.image.load('sunset.jpg').convert()
#backDropArea = backDrop.get_rect()


# Create the function that continues to show the images, otherwise they would disappear almost instantly.#
#def draw_em(): 
'''Put the letters on the screen'''
# Creates the variables the function call will need to show our background image.#
#the get_rect() function returns the position and size of our backDrop variable\image. 0,0 is the default position.
backDrop = pygame.image.load('sunset.jpg').convert()
backDropArea = backDrop.get_rect() 

# Creates the variables the function call needs to show our foreground images.#
letterA = pygame.image.load('A.png').convert()
letterA = pygame.transform.scale(letterA, (60, 60))
letterA.set_colorkey(BLACK)
square1_lett = letterA.get_rect(center=(screenSize_x -765, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterB = pygame.image.load('B.png').convert()
letterB = pygame.transform.scale(letterB, (60, 60))
letterB.set_colorkey(BLACK)
square2_lett = letterB.get_rect(center=(screenSize_x -665, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterC = pygame.image.load('C.png').convert()
letterC = pygame.transform.scale(letterC, (60, 60))
letterC.set_colorkey(BLACK)
square3_lett = letterC.get_rect(center=(screenSize_x -565, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterD = pygame.image.load('D.png').convert()
letterD = pygame.transform.scale(letterD, (60, 60))
letterD.set_colorkey(BLACK)
square4_lett = letterD.get_rect(center=(screenSize_x -465, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterE = pygame.image.load('E.png').convert()
letterE = pygame.transform.scale(letterE, (60, 60))
letterE.set_colorkey(BLACK)
square5_lett = letterE.get_rect(center=(screenSize_x -365, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterF = pygame.image.load('F.png').convert()
letterF = pygame.transform.scale(letterF, (60, 60))
letterF.set_colorkey(BLACK)
square6_lett = letterF.get_rect(center=(screenSize_x -265, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterG = pygame.image.load('G.png').convert()
letterG = pygame.transform.scale(letterG, (60, 60))
letterG.set_colorkey(BLACK)
square7_lett = letterG.get_rect(center=(screenSize_x -165, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterH = pygame.image.load('H.png').convert()
letterH = pygame.transform.scale(letterH, (60, 60))
letterH.set_colorkey(BLACK)
square8_lett = letterH.get_rect(center=(screenSize_x -65, screenSize_y - 165))

# Creates the variables the function call needs to show our foreground images.#
letterI = pygame.image.load('I.png').convert()
letterI = pygame.transform.scale(letterI, (60, 60))
letterI.set_colorkey(BLACK)
square9_lett = letterI.get_rect(center=(screenSize_x -715, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterJ = pygame.image.load('J.png').convert()
letterJ = pygame.transform.scale(letterJ, (60, 60))
letterJ.set_colorkey(BLACK)
square10_lett = letterJ.get_rect(center=(screenSize_x -615, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterK = pygame.image.load('K.png').convert()
letterK = pygame.transform.scale(letterK, (60, 60))
letterK.set_colorkey(BLACK)
square11_lett = letterK.get_rect(center=(screenSize_x -515, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterL = pygame.image.load('L.png').convert()
letterL = pygame.transform.scale(letterL, (60, 60))
letterL.set_colorkey(BLACK)
square12_lett = letterL.get_rect(center=(screenSize_x -415, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterM = pygame.image.load('M.png').convert()
letterM = pygame.transform.scale(letterM, (60, 60))
letterM.set_colorkey(BLACK)
square13_lett = letterM.get_rect(center=(screenSize_x -315, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterN = pygame.image.load('N.png').convert()
letterN = pygame.transform.scale(letterN, (60, 60))
letterN.set_colorkey(BLACK)
square14_lett = letterN.get_rect(center=(screenSize_x -215, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterO = pygame.image.load('O.png').convert()
letterO = pygame.transform.scale(letterO, (60, 60))
letterO.set_colorkey(BLACK)
square15_lett = letterO.get_rect(center=(screenSize_x -115, screenSize_y - 100))

# Creates the variables the function call needs to show our foreground images.#
letterP = pygame.image.load('P.png').convert()
letterP = pygame.transform.scale(letterP, (60, 60))
letterP.set_colorkey(BLACK)
square16_lett = letterP.get_rect(center=(screenSize_x -985, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterQ = pygame.image.load('Q.png').convert()
letterQ = pygame.transform.scale(letterQ, (60, 60))
letterQ.set_colorkey(BLACK)
square17_lett = letterQ.get_rect(center=(screenSize_x -905, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterR = pygame.image.load('R.png').convert()
letterR = pygame.transform.scale(letterR, (60, 60))
letterR.set_colorkey(BLACK)
square18_lett = letterR.get_rect(center=(screenSize_x -825, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterS = pygame.image.load('S.png').convert()
letterS = pygame.transform.scale(letterS, (60, 60))
letterS.set_colorkey(BLACK)
square19_lett = letterS.get_rect(center=(screenSize_x -745, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterT = pygame.image.load('T.png').convert()
letterT = pygame.transform.scale(letterT, (60, 60))
letterT.set_colorkey(BLACK)
square20_lett = letterT.get_rect(center=(screenSize_x -665, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterU = pygame.image.load('U.png').convert()
letterU = pygame.transform.scale(letterU, (60, 60))
letterU.set_colorkey(BLACK)
square21_lett = letterU.get_rect(center=(screenSize_x -585, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterV = pygame.image.load('V.png').convert()
letterV = pygame.transform.scale(letterV, (60, 60))
letterV.set_colorkey(BLACK)
square22_lett = letterV.get_rect(center=(screenSize_x -505, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterW = pygame.image.load('W.png').convert()
letterW = pygame.transform.scale(letterW, (60, 60))
letterW.set_colorkey(BLACK)
square23_lett = letterW.get_rect(center=(screenSize_x -425, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterX = pygame.image.load('X.png').convert()
letterX = pygame.transform.scale(letterX, (60, 60))
letterX.set_colorkey(BLACK)
square24_lett = letterX.get_rect(center=(screenSize_x -345, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterY = pygame.image.load('Y.png').convert()
letterY = pygame.transform.scale(letterY, (60, 60))
letterY.set_colorkey(BLACK)
square25_lett = letterY.get_rect(center=(screenSize_x -265, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
letterZ = pygame.image.load('Z.png').convert()
letterZ = pygame.transform.scale(letterZ, (60, 60))
letterZ.set_colorkey(BLACK)
square26_lett = letterZ.get_rect(center=(screenSize_x -185, screenSize_y - 35))

# Creates the variables the function call needs to show our foreground images.#
goButton = pygame.image.load('go.png').convert()
goButton = pygame.transform.scale(goButton, (140, 80))
goButton.set_colorkey(BLACK)
goButton_lett = goButton.get_rect(center=(screenSize_x -945, screenSize_y - 130))


# Creates the variables the function call needs to show our foreground images.#
doneButton = pygame.image.load('done.png').convert()
doneButton = pygame.transform.scale(doneButton, (30, 215))
doneButton.set_colorkey(BLACK)
doneButton_lett = doneButton.get_rect(center=(screenSize_x -25, screenSize_y -400))


width=1024;
height=600
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('Random Letters')
redSquare = pygame.image.load("sunset.jpg").convert()
 
x = 0; # x coordnate of image
y = 0; # y coordinate of image
#screen.blit(redSquare ,  ( x,y)) # paint to screen
#pygame.display.flip() # paint screen one time

chosenLetts=[]
finishedWords=[]
cleanedWords=""

game_time = pygame.time.get_ticks()
print(game_time)

running = True
while (running) and game_time < 40000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game_time = pygame.time.get_ticks()
        
        
        
   #     draw_em()
        # Color in the background.# 
        DISPLAYSURF.fill(BLACK)
        
        # Display the background image.#
        DISPLAYSURF.blit(backDrop, backDropArea)

        # Display the foreground image(s).#
        DISPLAYSURF.blit(letterA, square1_lett)
        DISPLAYSURF.blit(letterB, square2_lett)
        DISPLAYSURF.blit(letterC, square3_lett)
        DISPLAYSURF.blit(letterD, square4_lett)
        DISPLAYSURF.blit(letterE, square5_lett)
        DISPLAYSURF.blit(letterF, square6_lett)
        DISPLAYSURF.blit(letterG, square7_lett)
        DISPLAYSURF.blit(letterH, square8_lett)
        DISPLAYSURF.blit(letterI, square9_lett)
        DISPLAYSURF.blit(letterJ, square10_lett)
        DISPLAYSURF.blit(letterK, square11_lett)
        DISPLAYSURF.blit(letterL, square12_lett)
        DISPLAYSURF.blit(letterM, square13_lett)
        DISPLAYSURF.blit(letterN, square14_lett)
        DISPLAYSURF.blit(letterO, square15_lett)
        DISPLAYSURF.blit(letterP, square16_lett)
        DISPLAYSURF.blit(letterQ, square17_lett)
        DISPLAYSURF.blit(letterR, square18_lett)
        DISPLAYSURF.blit(letterS, square19_lett)
        DISPLAYSURF.blit(letterT, square20_lett)
        DISPLAYSURF.blit(letterU, square21_lett)
        DISPLAYSURF.blit(letterV, square22_lett)
        DISPLAYSURF.blit(letterW, square23_lett)
        DISPLAYSURF.blit(letterX, square24_lett)
        DISPLAYSURF.blit(letterY, square25_lett)
        DISPLAYSURF.blit(letterZ, square26_lett)        

        DISPLAYSURF.blit(goButton, goButton_lett)

        DISPLAYSURF.blit(doneButton, doneButton_lett)
        #this next section shows the timer and a notice that 40000 marks the end of the game

        #choose a font
        myfont = pygame.font.SysFont('Courier New', 25)
        #create a variable, use the font to print game_time, convert game_time to a string, set the color of the text
        showticks=myfont.render(str(game_time), True, (255,0,0))
        #actually show the text on the screen
        screen.blit(showticks, (300, 25))
        #create a variable to use the same font to tell the user when the game ends, set the color of the text
        showtimenotice=myfont.render('Game ends at 40000', True, (255,0,0))
        #show the message on the screen
        screen.blit(showtimenotice, (300, 40))
        titleFont = pygame.font.Font('freesansbold.ttf', 80)
        titleFont.set_underline(True)
        
        showgamename=titleFont.render("Random Letters", True, (0, 255, 255))
        screen.blit(showgamename, (20, 65))
                                                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] >= 230 and mouse_position[0] <= 288:
                    if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                        print('clicked on A', mouse_position)
                        chosenLetts.append("a")
                        print(chosenLetts)
                        
            if mouse_position[0] >= 330 and mouse_position[0] <= 385:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on B', mouse_position)
                    chosenLetts.append("b")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 429 and mouse_position[0] <= 488:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on C', mouse_position)
                    chosenLetts.append("c")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 530 and mouse_position[0] <= 588:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on D', mouse_position)
                    chosenLetts.append("d")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 630 and mouse_position[0] <= 688:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on E', mouse_position)
                    chosenLetts.append("e")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 730 and mouse_position[0] <= 785:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on F', mouse_position)
                    chosenLetts.append("f")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 830 and mouse_position[0] <= 888:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on G', mouse_position)
                    chosenLetts.append("g")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 930 and mouse_position[0] <= 987:
                if mouse_position[1] >= 405 and mouse_position[1] <= 465: 
                    print('clicked on H', mouse_position)
                    chosenLetts.append("h")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 279 and mouse_position[0] <= 338:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on I', mouse_position)
                    chosenLetts.append("i")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 378 and mouse_position[0] <= 437:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on J', mouse_position)
                    chosenLetts.append("j")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 479 and mouse_position[0] <= 537:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on K', mouse_position)
                    chosenLetts.append("k")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 577 and mouse_position[0] <= 638:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on L', mouse_position)
                    chosenLetts.append("l")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 678 and mouse_position[0] <= 737:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on M', mouse_position)
                    chosenLetts.append("m")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 777 and mouse_position[0] <= 835:
                if mouse_position[1] >= 470 and mouse_position[1] <= 530: 
                    print('clicked on N', mouse_position)
                    chosenLetts.append("n")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 877 and mouse_position[0] <= 937:
                if mouse_position[1] >= 475 and mouse_position[1] <= 530: 
                    print('clicked on O', mouse_position)
                    chosenLetts.append("o")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 9 and mouse_position[0] <= 68:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on P', mouse_position)
                    chosenLetts.append("p")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 90 and mouse_position[0] <= 148:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on Q', mouse_position)
                    chosenLetts.append("q")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 169 and mouse_position[0] <= 228:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on R', mouse_position)
                    chosenLetts.append("r")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 249 and mouse_position[0] <= 308:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on S', mouse_position)
                    chosenLetts.append("s")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 329 and mouse_position[0] <= 388:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on T', mouse_position)
                    chosenLetts.append("t")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 409 and mouse_position[0] <= 468:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on U', mouse_position)
                    chosenLetts.append("u")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 489 and mouse_position[0] <= 548:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on V', mouse_position)
                    chosenLetts.append("v")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 569 and mouse_position[0] <= 628:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on W', mouse_position)
                    chosenLetts.append("w")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 649 and mouse_position[0] <= 708:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on X', mouse_position)
                    chosenLetts.append("x")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 729 and mouse_position[0] <= 789:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on Y', mouse_position)
                    chosenLetts.append("y")
                    print(chosenLetts)
                    
            if mouse_position[0] >= 809 and mouse_position[0] <= 869:
                if mouse_position[1] >= 535 and mouse_position[1] <= 594: 
                    print('clicked on Z', mouse_position)
                    chosenLetts.append("z")
                    print(chosenLetts)

            if mouse_position[0] >= 10 and mouse_position[0] <= 146:
                if mouse_position[1] >= 431 and mouse_position[1] <= 509: 
                    print('clicked on GO', mouse_position)
                    #chosenLetts.append("GO")
                    #print(chosenLetts)
                    #finishedWords.append(chosenLetts)
                    #print(finishedWords)
                    #wordLength=len(chosenLetts)
                    #for i in range(wordLength):
                    #    finishedWords=finishedWords + (chosenLetts[i] + chosenLetts[i+1])
                    #finishedWords = ''.join(chosenLetts)
                    #finishedWords = " " + finishedWords
                    finishedWords.append(chosenLetts)
                    print("chosenLetts= ", chosenLetts)
                    cleanedWords = ''.join(chosenLetts)
                    print("marker", cleanedWords)
                    saveWord = cleanedWords
                    f=open("Output.txt","a+")
                    f.write(cleanedWords + '\n')
                    f.close()
                    chosenLetts=[]
                    print("finishedWords ", finishedWords)
                    cleanedWords = ''.join(chosenLetts)
                    mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="MH575-yes", database="letters")
                    cursor = mydb.cursor()
                    query = "INSERT INTO game_records (name, date_time, game_type, ip, word, good_word, bad_word, secure_code, points, level, license, renewal, donations, scoreboard, username, highscore, average, spare, spare_two, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    myname = "Llama"
                    values = (myname, '2020-08-13 21:30:00', '1', '192.168.0.1', 'work', saveWord, 'nope', '12345', '1', '1', '0', '2030', '100', '1', 'ausersname', '1', '1.00', 'holder1', 'holder2', 'nope.noway@gmail.com')
                    cursor.execute(query, values)
                    mydb.commit()

            if mouse_position[0] >= 985 and mouse_position[0] <= 1015:
                if mouse_position[1] >= 94 and mouse_position[1] <= 309: 
                    print('clicked on DONE', mouse_position)
                    #chosenLetts.append("GO")
                    #print(chosenLetts)
                    #finishedWords.append(chosenLetts)
                    #print(finishedWords)
                    #wordLength=len(chosenLetts)
                    #for i in range(wordLength):
                    #    finishedWords=finishedWords + (chosenLetts[i] + chosenLetts[i+1])
                    #finishedWords = ''.join(chosenLetts)
                    #finishedWords = " " + finishedWords
                    finishedWords.append(chosenLetts)
                    print("chosenLetts= ", chosenLetts)
                    cleanedWords = ''.join(chosenLetts)
                    print(cleanedWords)
                    f=open("Output.txt","a+")
                    f.write(cleanedWords)
                    f.close()
                    chosenLetts=[]
                    print("finishedWords ", finishedWords)
                    cleanedWords = ''.join(chosenLetts)
                   
                    sleep(1)
                    running=False

        if event.type == pygame.KEYDOWN:
                 if event.key==K_a:
                     print('typed a')
                     chosenLetts.append("a")
                     print(chosenLetts)
                 if event.key==K_b:
                     print('typed b')
                     chosenLetts.append("b")
                     print(chosenLetts)
                 if event.key==K_c:
                     print('typed c')
                     chosenLetts.append("c")
                     print(chosenLetts)
                 if event.key==K_d:
                     print('typed d')
                     chosenLetts.append("d")
                     print(chosenLetts)
                 if event.key==K_e:
                     print('typed e')
                     chosenLetts.append("e")
                     print(chosenLetts)
                 if event.key==K_f:
                     print('typed f')
                     chosenLetts.append("f")
                     print(chosenLetts)
                 if event.key==K_g:
                     print('typed g')
                     chosenLetts.append("g")
                     print(chosenLetts)
                 if event.key==K_h:
                     print('typed h')
                     chosenLetts.append("h")
                     print(chosenLetts)
                 if event.key==K_i:
                     print('typed i')
                     chosenLetts.append("i")
                     print(chosenLetts)
                 if event.key==K_j:
                     print('typed j')
                     chosenLetts.append("j")
                     print(chosenLetts)
                 if event.key==K_k:
                     print('typed k')
                     chosenLetts.append("k")
                     print(chosenLetts)
                 if event.key==K_l:
                     print('typed l')
                     chosenLetts.append("l")
                     print(chosenLetts)
                 if event.key==K_m:
                     print('typed m')
                     chosenLetts.append("m")
                     print(chosenLetts)
                 if event.key==K_n:
                     print('typed n')
                     chosenLetts.append("n")
                     print(chosenLetts)
                 if event.key==K_o:
                     print('typed o')
                     chosenLetts.append("o")
                     print(chosenLetts)
                 if event.key==K_p:
                     print('typed p')
                     chosenLetts.append("p")
                     print(chosenLetts)
                 if event.key==K_q:
                     print('typed q')
                     chosenLetts.append("q")
                     print(chosenLetts)
                 if event.key==K_r:
                     print('typed r')
                     chosenLetts.append("r")
                     print(chosenLetts)
                 if event.key==K_s:
                     print('typed s')
                     chosenLetts.append("s")
                     print(chosenLetts)
                 if event.key==K_t:
                     print('typed t')
                     chosenLetts.append("t")
                     print(chosenLetts)
                 if event.key==K_u:
                     print('typed u')
                     chosenLetts.append("u")
                     print(chosenLetts)
                 if event.key==K_v:
                     print('typed v')
                     chosenLetts.append("v")
                     print(chosenLetts)
                 if event.key==K_w:
                     print('typed w')
                     chosenLetts.append("w")
                     print(chosenLetts)
                 if event.key==K_x:
                     print('typed x')
                     chosenLetts.append("x")
                     print(chosenLetts)
                 if event.key==K_y:
                     print('typed y')
                     chosenLetts.append("y")
                     print(chosenLetts)
                 if event.key==K_z:
                     print('typed z')
                     chosenLetts.append("z")
                     print(chosenLetts)
                 if event.key==K_RETURN:
                     print("You did hit Enter")
                     finishedWords.append(chosenLetts)
                     print("chosenLetts= ", chosenLetts)
                     cleanedWords = ''.join(chosenLetts)
                     print("marker", cleanedWords)
                     saveWord = cleanedWords
                     f=open("Output.txt","a+")
                     f.write(cleanedWords + '\n')
                     f.close()
                     chosenLetts=[]
                     print("finishedWords ", finishedWords)
                     cleanedWords = ''.join(chosenLetts)
                     mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="MH575-yes", database="letters")
                     cursor = mydb.cursor()
                     query = "INSERT INTO game_records (name, date_time, game_type, ip, word, good_word, bad_word, secure_code, points, level, license, renewal, donations, scoreboard, username, highscore, average, spare, spare_two, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                     myname = "Dolly Llama"
                     values = (myname, '2020-08-27 21:33:00', '1', '192.168.0.1', 'work', saveWord, 'nope', '12345', '1', '1', '0', '2030', '100', '1', 'ausersname', '1', '1.00', 'holder1', 'holder2', 'nope.noway@gmail.com')
                     cursor.execute(query, values)
                     mydb.commit()
                 if event.key==K_ESCAPE:
                     print("You Escaped!")
                     finishedWords.append(chosenLetts)
                     print("chosenLetts= ", chosenLetts)
                     cleanedWords = ''.join(chosenLetts)
                     print("marker", cleanedWords)
                     saveWord = cleanedWords
                     f=open("Output.txt","a+")
                     f.write(cleanedWords + '\n')
                     f.close()
                     chosenLetts=[]
                     print("finishedWords ", finishedWords)
                     cleanedWords = ''.join(chosenLetts)
                     mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="MH575-yes", database="letters")
                     cursor = mydb.cursor()
                     query = "INSERT INTO game_records (name, date_time, game_type, ip, word, good_word, bad_word, secure_code, points, level, license, renewal, donations, scoreboard, username, highscore, average, spare, spare_two, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                     myname = "Bolly GLlamar"
                     values = (myname, '2020-08-27 22:15:00', '1', '192.168.0.1', 'work', saveWord, 'nope', '12345', '1', '1', '0', '2030', '100', '1', 'ausersname', '1', '1.00', 'holder1', 'holder2', 'nope.noway@gmail.com')
                     cursor.execute(query, values)
                     mydb.commit()

                     sleep(1)
                     running=False
               
    pygame.display.flip() # paint screen one time
#loop over, quit pygame
print("repeat" , finishedWords)
pygame.quit()
