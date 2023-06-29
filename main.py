import time
import pygame
import os

screenLength = 850
screenHeight = 450
dim_field = (screenLength, screenHeight)

screen = pygame.display.set_mode(dim_field)
# BACKGROUND LEVEL 1
background = pygame.image.load(os.path.join("assets", "background.png"))
background = pygame.transform.scale(background, dim_field)
# BACKGROUND LEVEL 2
background1 = pygame.image.load(os.path.join("assets", "background1.png"))
background1 = pygame.transform.scale(background1, dim_field)

# text
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)
# WIN TEXT LEVEL 1
level1WinText = font.render("Congratulations! You completed this level!", True, (255, 255, 255))
winText2 = font.render("Press SPACE to continue to Level 2!", True, (255, 255, 255))
# WIN TEXT LEVEL 2
level2WinText = font.render("Congratulations! You completed the game!", True, (255, 255, 255))
# DEATH TEXT
deathText = font.render("Sorry, you died. Try again.", True, (255, 255, 255))

# flag
flagSprite = pygame.image.load(os.path.join("assets", "flagSprite.png")).convert()
flagSprite = pygame.transform.scale(flagSprite, (70, 100))
rect_flag = pygame.Rect(770, 345, 70, 100)
flagSprite.set_colorkey((0, 0, 0))
# acorn
acornSprite = pygame.image.load(os.path.join("assets", "acorn.png")).convert()
acornWidth = 20
acornHeight = 25
acornSprite = pygame.transform.scale(acornSprite, (acornWidth, acornHeight))
acornSprite.set_colorkey((0, 0, 0))
# ACORN LEVEL 1
rectAcorn1 = pygame.Rect(120, 275, acornWidth, acornHeight)
rectAcorn2 = pygame.Rect(265, 275, acornWidth, acornHeight)
rectAcorn3 = pygame.Rect(505, 150, acornWidth, acornHeight)
rectAcorn4 = pygame.Rect(615, 200, acornWidth, acornHeight)
# ACORN LEVEL 2
rectAcorn5 = pygame.Rect(290, 215, acornWidth, acornHeight)
rectAcorn6 = pygame.Rect(460, 85, acornWidth, acornHeight)
rectAcorn7 = pygame.Rect(385, 85, acornWidth, acornHeight)
rectAcorn8 = pygame.Rect(385, 60, acornWidth, acornHeight)
rectAcorn9 = pygame.Rect(465, 325, acornWidth, acornHeight)
rectAcorn10 = pygame.Rect(590, 225, acornWidth, acornHeight)
# plants
plantSprite = pygame.image.load(os.path.join("assets", "plant.png")).convert()
plantWidth = 38
plantHeight = 25
plantSprite = pygame.transform.scale(plantSprite, (plantWidth, plantHeight))
plantSprite.set_colorkey((255, 255, 255))
# PLANT LEVEL 1
rectPlant1 = pygame.Rect(190, 275, plantWidth, plantHeight)
rectPlant2 = pygame.Rect(250, 415, plantWidth, plantHeight)
rectPlant3 = pygame.Rect(385, 150, plantWidth, plantHeight)
rectPlant4 = pygame.Rect(545, 250, plantWidth, plantHeight)
# PLANT LEVEL 2
rectPlant5 = pygame.Rect(150, 215, plantWidth, plantHeight)
rectPlant6 = pygame.Rect(200, 215, plantWidth, plantHeight)
rectPlant7 = pygame.Rect(350, 325, plantWidth, plantHeight)
rectPlant8 = pygame.Rect(655, 225, plantWidth, plantHeight)
# deer
deerSprite = pygame.image.load(os.path.join("assets", "deer.png")).convert()
deerSprite = pygame.transform.scale(deerSprite, (70, 80))
deerSprite.set_colorkey((14, 14, 14))
rect_deer = pygame.Rect(0, 362, 70, 80)
# ground
rect_ground = pygame.Rect(0, 440, screenLength, 10)
# platforms LEVEL 1
rectPlatform1 = pygame.Rect(100, 300, 250, 15)
rectPlatform2 = pygame.Rect(345, 175, 200, 15)
rectPlatform3 = pygame.Rect(530, 275, 150, 15)
# PLATFORMS LEVEL 2
rectPlatform4 = pygame.Rect(120, 240, 225, 15)
rectPlatform5 = pygame.Rect(330, 350, 200, 15)
rectPlatform6 = pygame.Rect(350, 110, 180, 15)
rectPlatform7 = pygame.Rect(575, 250, 150, 15)
# instructions
instructionsSprite = pygame.image.load(os.path.join("assets", "instructions.png")).convert()
instructionsSprite = pygame.transform.scale(instructionsSprite, (650, 400))
rect_instructions = pygame.Rect(105, 20, 650, 400)
# lists

level1 = True
level2 = False
qPressed = False
FPS = 30
stepsize = 5
gravityImpact = 6
clock = pygame.time.Clock()


def reset():
  global acorn1, acorn2, acorn3, acorn4, acorn5, acorn6, acorn7, acorn8, acorn9, acorn10, rect_deer, acornList, plantList, platformList, winText
  acorn1 = True
  acorn2 = True
  acorn3 = True
  acorn4 = True
  acorn5 = True
  acorn6 = True
  acorn7 = True
  acorn8 = True
  acorn9 = True
  acorn10 = True

  rect_deer = pygame.Rect(0, 362, 72, 78)
  if (level1):
    acornList = [rectAcorn1, rectAcorn2, rectAcorn3, rectAcorn4]
    plantList = [rectPlant1, rectPlant2, rectPlant3, rectPlant4]
    platformList = [rect_ground, rectPlatform1, rectPlatform2, rectPlatform3, rect_flag]
    winText = level1WinText

  if (level2):
    acornList = [rectAcorn5, rectAcorn6, rectAcorn7, rectAcorn8, rectAcorn9, rectAcorn10]
    plantList = [rectPlant5, rectPlant6, rectPlant7, rectPlant8]
    platformList = [rect_ground, rectPlatform4, rectPlatform5, rectPlatform6, rectPlatform7, rect_flag]
    winText = level2WinText


# Game loop
while (qPressed == False):
  # LEVEL 1 START
  while (level1):
    screen.fill((0, 0, 0))
    screen.blit(instructionsSprite, rect_instructions)
    pygame.display.update()
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
      break
  # break
  reset()
  while (level1):
    clock.tick(FPS)
    gameWon = False
    gameLost = False
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
      qPressed = True
      break
    # Key controls
    if keys[pygame.K_LEFT]:
      rect_deer.move_ip(-stepsize, 0)
    elif keys[pygame.K_RIGHT]:
      rect_deer.move_ip(stepsize, 0)
    elif keys[pygame.K_UP]:
      rect_deer.move_ip(3, -stepsize)
    elif keys[pygame.K_DOWN]:
      rect_deer.move_ip(0, stepsize)
    else:
      rect_deer.move_ip(0, gravityImpact)

    # collision lists
    collideIndexPlatform = rect_deer.collidelist(platformList)
    collideIndexAcorn = rect_deer.collidelist(acornList)
    collideIndexPlant = rect_deer.collidelist(plantList)

    # platform collisions
    if collideIndexPlatform == 0 or collideIndexPlatform == 1 or collideIndexPlatform == 2 or collideIndexPlatform == 3:
      rect_deer.bottom = platformList[collideIndexPlatform].top
    if collideIndexPlatform == 4:
      gameWon = True

    # acorn collisions
    if collideIndexAcorn == 0:
      acorn1 = False
    if collideIndexAcorn == 1:
      acorn2 = False
    if collideIndexAcorn == 2:
      acorn3 = False
    if collideIndexAcorn == 3:
      acorn4 = False

    # plant collisions
    if collideIndexPlant >= 0:
      gameLost = True

    # deer boundaries
    if rect_deer.left <= 0:
      rect_deer.move_ip(stepsize, 0)
    if rect_deer.right >= screenLength:
      rect_deer.move_ip(-stepsize, 0)
    if rect_deer.top <= 0:
      rect_deer.move_ip(0, stepsize)
    if rect_deer.bottom >= screenHeight:
      rect_deer.move_ip(0, -stepsize)

    screen.blit(background, (0, 0))

    # draw ground
    pygame.draw.rect(screen, (118, 127, 182), rect_ground)
    # draw platforms
    pygame.draw.rect(screen, (79, 249, 243), rectPlatform1)
    pygame.draw.rect(screen, (79, 249, 243), rectPlatform2)
    pygame.draw.rect(screen, (79, 249, 243), rectPlatform3)

    if (acorn1):
      screen.blit(acornSprite, rectAcorn1)
    if (acorn2):
      screen.blit(acornSprite, rectAcorn2)
    if (acorn3):
      screen.blit(acornSprite, rectAcorn3)
    if (acorn4):
      screen.blit(acornSprite, rectAcorn4)

    screen.blit(plantSprite, rectPlant1)
    screen.blit(plantSprite, rectPlant2)
    screen.blit(plantSprite, rectPlant3)
    screen.blit(plantSprite, rectPlant4)

    screen.blit(deerSprite, rect_deer)
    screen.blit(flagSprite, rect_flag)

    # draw text
    if (gameWon):
      screen.fill((0, 0, 0))
      screen.blit(winText, (75, 180))
      screen.blit(winText2, (125, 230))
    elif (gameLost):
      screen.fill((0, 0, 0))
      screen.blit(deathText, (190, 200))

    pygame.display.update()
    if (gameLost):
      time.sleep(2)
      break

    while (gameWon):
      pygame.event.get()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        level2 = True
        level1 = False
        break

  # LEVEL 2 START
  while (level2):
    reset()
    break
  while (level2):
    clock.tick(FPS)
    gameWon = False
    gameLost = False
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
      qPressed = True
      break
    # Key controls
    if keys[pygame.K_LEFT]:
      rect_deer.move_ip(-stepsize, 0)
    elif keys[pygame.K_RIGHT]:
      rect_deer.move_ip(stepsize, 0)
    elif keys[pygame.K_UP]:
      rect_deer.move_ip(3, -stepsize)
    elif keys[pygame.K_DOWN]:
      rect_deer.move_ip(0, stepsize)
    else:
      rect_deer.move_ip(0, gravityImpact)

    # collision lists
    collideIndexPlatform = rect_deer.collidelist(platformList)
    collideIndexAcorn = rect_deer.collidelist(acornList)
    collideIndexPlant = rect_deer.collidelist(plantList)

    # platform collisions
    if collideIndexPlatform == 0 or collideIndexPlatform == 1 or collideIndexPlatform == 2 or collideIndexPlatform == 3 or collideIndexPlatform == 4:
      rect_deer.bottom = platformList[collideIndexPlatform].top
    if collideIndexPlatform == 5:
      gameWon = True

    # acorn collisions
    if collideIndexAcorn == 0:
      acorn5 = False
    if collideIndexAcorn == 1:
      acorn6 = False
    if collideIndexAcorn == 2:
      acorn7 = False
    if collideIndexAcorn == 3:
      acorn8 = False
    if collideIndexAcorn == 4:
      acorn9 = False
    if collideIndexAcorn == 5:
      acorn10 = False

    # plant collisions
    if collideIndexPlant >= 0:
      gameLost = True

    # deer boundaries
    if rect_deer.left <= 0:
      rect_deer.move_ip(stepsize, 0)
    if rect_deer.right >= screenLength:
      rect_deer.move_ip(-stepsize, 0)
    if rect_deer.top <= 0:
      rect_deer.move_ip(0, stepsize)
    if rect_deer.bottom >= screenHeight:
      rect_deer.move_ip(0, -stepsize)

    screen.blit(background1, (0, 0))

    # draw ground
    pygame.draw.rect(screen, (118, 127, 182), rect_ground)
    # draw platforms
    pygame.draw.rect(screen, (118, 127, 182), rectPlatform4)
    pygame.draw.rect(screen, (118, 127, 182), rectPlatform5)
    pygame.draw.rect(screen, (118, 127, 182), rectPlatform6)
    pygame.draw.rect(screen, (118, 127, 182), rectPlatform7)

    # draw acorns and make them disappear
    if (acorn5):
      screen.blit(acornSprite, rectAcorn5)
    if (acorn6):
      screen.blit(acornSprite, rectAcorn6)
    if (acorn7):
      screen.blit(acornSprite, rectAcorn7)
    if (acorn8):
      screen.blit(acornSprite, rectAcorn8)
    if (acorn9):
      screen.blit(acornSprite, rectAcorn9)
    if (acorn10):
      screen.blit(acornSprite, rectAcorn10)

    # draw plants
    screen.blit(plantSprite, rectPlant5)
    screen.blit(plantSprite, rectPlant6)
    screen.blit(plantSprite, rectPlant7)
    screen.blit(plantSprite, rectPlant8)

    # draw deer
    screen.blit(deerSprite, rect_deer)
    # draw flag
    screen.blit(flagSprite, rect_flag)

    # draw text
    if (gameWon):
      screen.fill((0, 0, 0))
      screen.blit(winText, (75, 200))
    elif (gameLost):
      screen.fill((0, 0, 0))
      screen.blit(deathText, (190, 200))

    pygame.display.update()
    if (gameLost or gameWon):
      time.sleep(2)
      break

  if (gameWon):
    break

pygame.display.quit()